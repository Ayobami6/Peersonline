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
    """ This function is used to render the askgpt view
    """
    # get user id from request
    user = request.user
    # get the openai api key from user profile
    user_id = user.id
    api_key_encrpted = user.profile.openai_key
    # decrypt the api key if its encrypted
    if api_key_encrpted:
        api_key = decrypt_data(api_key_encrpted)
        cache.set("encrypted_key", api_key, timeout=3600)

    data = "AskGpt is an AI assistant that is an expert in Software \
        Engineering. You can ask it questions about \
            Software Engineering and it will \
                give you an answer. \n \
                    Example: \n \
                        What is a variable? \n \
                            "
    if request.method == "POST":
        openai.api_key = api_key
        user_query = request.POST.get('user_query')
        user_prompt = user_query
        chat_response = openai.Completion.create(
            model="text-davinci-003",
            prompt="You are an AI assisstant that is an Expert in Software \
            engineering\nYou know about Software Engineering\nYou can provide \
            advice on Linux, Programming Languages, Software Engineering \
            Concepts and Education.\n If possible make references\n\
            to publications for further reading by appending the \
            name of the publication to this \
            exact url https://annas-archive.org/search?q= \
            do not change anything in the url just append the publication\
            name for example: \
            https://annas-archive.org/search?q=flask web development by \
            Grinberg, Miguel. You must critically \
            percieve the question and make sure\
            the question is related \
            to software engineering before you provide an answer,\
            however, If the question is not related to sofware \
            engineering at all! please\
            respond with the phrase \"I'm just an expert \
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
