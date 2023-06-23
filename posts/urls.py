from django.urls import path
from .views import CreatePostView, PostDetailView, PostUpateView
from .views import PostDeleteView, like_view, search_view

urlpatterns = [
    path('home/create_post', CreatePostView.as_view(), name='create_post'),
    path('home/post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('home/post/<int:pk>/update', PostUpateView.as_view(),
         name='post_update'),
    path('home/post/<int:pk>/delete', PostDeleteView.as_view(),
         name='post_delete'),
    path('like/<int:pk>', like_view, name='like'),
    path('search', search_view, name='search'),

]
