# Generated by Django 4.0.5 on 2022-06-14 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
