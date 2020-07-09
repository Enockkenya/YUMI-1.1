# Generated by Django 2.0.5 on 2020-07-09 10:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adverts', '0013_auto_20200707_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='Advert',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='advert',
            name='likes',
            field=models.ManyToManyField(related_name='item_condition', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
