# Generated by Django 5.0.4 on 2024-05-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]