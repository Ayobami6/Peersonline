from django.shortcuts import render
import openai
import os
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dotenv import load_dotenv
from . forms import AskGPTForm
from utils.encryption import decrypt_data
from django.core.cache import cache


@login_required(login_url="/home/login")
def askgpt_view(request):
    # get user id from request
    user = request.user
    # get the openai api key from user profile
    user_id = user.id
    api_key_encrpted = user.profile.openai_key
    cached_key = cache.get("encrypted_key")
    if not cached_key:
        # decrypt the api key
        if api_key_encrpted:
            api_key = decrypt_data(api_key_encrpted)
            cache.set("encrypted_key", api_key, timeout=3600)

    data = None
    if request.method == "POST":
        openai.api_key = cached_key
        user_query = request.POST.get('user_query')
        user_prompt = user_query
        chat_response = openai.Completion.create(
            model="text-davinci-003",
            prompt="You are an AI assisstant that is an Expert in Software \
            engineering\nYou know about Software Engineering\nYou can provide \
            advice on Linux, Programming Languages, Software Engineering \
            Concepts and Education\n\nIf you are unable to provide an answer \
            to a question please respond with the phrase \"I'm just an expert \
            in Software engineering, can't help with \
            that\n\n " + "\n" + user_prompt,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.73,
            presence_penalty=0
        )
        data = chat_response['choices'][0]['text'].replace("?", "")
    return render(request, 'askgpt/askgpt.html', {'response': data})
