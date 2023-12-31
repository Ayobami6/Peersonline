# Generated by Django 4.1.7 on 2023-06-23 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorSession',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True, serialize=False,
                                     verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('topic_title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('venue_link', models.CharField(max_length=250)),
                ('mentor', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
