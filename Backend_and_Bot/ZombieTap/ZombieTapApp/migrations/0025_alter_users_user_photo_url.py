# Generated by Django 5.0.6 on 2024-07-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZombieTapApp', '0024_alter_users_user_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_photo_url',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
