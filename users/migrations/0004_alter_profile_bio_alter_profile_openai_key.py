# Generated by Django 4.1.7 on 2023-06-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='openai_key',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]