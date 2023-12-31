# Generated by Django 4.1.7 on 2023-06-23 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsession',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mentorsession',
            name='mentor_full_name',
            field=models.CharField(default=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL), max_length=250),
        ),
        migrations.AddField(
            model_name='mentorsession',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorsession',
            name='venue',
            field=models.CharField(default='Now', max_length=250),
            preserve_default=False,
        ),
    ]
