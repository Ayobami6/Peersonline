from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Posts
from .forms import PostsForms
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.


class CreatePostView(LoginRequiredMixin, CreateView):
    """ This class is used to create a post """
    model = Posts
    form_class = PostsForms
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """ This method is used to validate the form """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    """ This class is used to view a single post """
    model = Posts
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        """ This method is used to get the context data """
        context = super().get_context_data(**kwargs)
        post = Posts.objects.get(id=self.kwargs['pk'])
        total_likes = post.total_likes()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class PostUpateView(LoginRequiredMixin, UpdateView):
    """ This class is used to update a post """
    model = Posts
    form_class = PostsForms
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('home')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """ This class is used to delete a post """
    model = Posts
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')


def like_view(request, pk):
    """ This function is used to like a post and unlike a post
    """
    # get the post
    post = Posts.objects.get(id=pk)
    # check the post if the user has liked it
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    post.refresh_from_db()
    total_likes = post.total_likes()
    data = {
        'total_likes': total_likes,
    }
    return JsonResponse(data)


def search_view(request):
    """ This function is used to search a post """
    query = request.GET.get('query')
    posts = Posts.objects.filter(title__icontains=query)
    context = {
        'posts': list(posts.values()),
    }
    return JsonResponse(context)
