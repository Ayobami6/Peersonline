# Generated by Django 4.1.7 on 2023-06-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_openai_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='openai_key',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
