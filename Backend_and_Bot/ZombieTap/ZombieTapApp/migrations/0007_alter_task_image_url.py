# Generated by Django 5.0.6 on 2024-07-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZombieTapApp', '0006_task_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image_url',
            field=models.URLField(default='https://web.telegram.org/e799b216-378f-4e0a-98b4-764da627af65g', max_length=10000000),
        ),
    ]
