# Generated by Django 5.0.6 on 2024-07-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZombieTapApp', '0004_alter_task_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=1000),
        ),
    ]
