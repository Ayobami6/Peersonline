from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.encryption import encrypt_data
# Create your models here.


class Profile(models.Model):
    """ This class is used to create a profile for a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_img',
        blank=True, default='profile_img/default.png')
    openai_key = models.CharField(max_length=50000, blank=True)

    def save(self, *args, **kwargs):
        """ Overwrite the save method to encrypt the openai_key
        """
        if self.openai_key:
            self.openai_key = encrypt_data(self.openai_key)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'

    # create a profile for a user when they are created using django signals
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """ Create a profile for a user when they are created
        """
        if created:
            Profile.objects.create(user=instance)

    # save the profile for a user when they are created using django signals
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """ Save the profile for a user when they are created
        """
        instance.profile.save()
