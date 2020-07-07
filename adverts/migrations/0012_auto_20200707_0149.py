# Generated by Django 2.0.5 on 2020-07-07 01:49

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0011_merge_20200707_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviewee',
            new_name='adseller',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='tags',
        ),
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advert',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_review', to=settings.AUTH_USER_MODEL),
        ),
    ]
