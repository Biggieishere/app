# Generated by Django 5.0.4 on 2024-05-21 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_contacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]
