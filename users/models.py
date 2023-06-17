from django.db import models
from cryptography.fernet import Fernet
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

encryption_key = Fernet.generate_key()


class Profile(models.Model):
    """ This class is used to create a profile for a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics',
        blank=True, default='profile_pics/default.png')
    openai_key = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        """ Overwrite the save method to encrypt the openai_key
        """
        f = Fernet(encryption_key)
        self.openai_key = f.encrypt(self.openai_key.encode()).decode()
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
