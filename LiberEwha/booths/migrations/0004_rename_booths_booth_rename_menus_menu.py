# Generated by Django 5.1.1 on 2024-09-23 16:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booths', '0003_rename_thumnail_booths_thumbnail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booths',
            new_name='Booth',
        ),
        migrations.RenameModel(
            old_name='Menus',
            new_name='Menu',
        ),
    ]