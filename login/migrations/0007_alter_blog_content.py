# Generated by Django 5.0.4 on 2024-05-15 15:42

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
