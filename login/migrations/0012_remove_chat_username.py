# Generated by Django 5.0.4 on 2024-05-17 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_chat_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='username',
        ),
    ]
