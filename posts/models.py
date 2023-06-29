from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your models here.


class Posts(models.Model):
    """ This class is used to create a post table in the database """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def total_likes(self):
        """ Return the total number of likes for a post """
        return self.likes.count()

    def __str__(self):
        """ Return the title and author of the post """
        return f"{self.title} by {self.author.username}"
