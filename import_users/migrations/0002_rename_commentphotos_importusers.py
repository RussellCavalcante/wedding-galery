# Generated by Django 4.2.7 on 2023-11-03 11:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('import_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentPhotos',
            new_name='ImportUsers',
        ),
    ]
