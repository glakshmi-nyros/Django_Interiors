# Generated by Django 3.0.1 on 2020-01-17 04:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modsy', '0013_auto_20200116_0927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Requirement',
            new_name='project',
        ),
    ]
