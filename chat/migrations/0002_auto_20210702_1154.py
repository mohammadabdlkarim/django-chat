# Generated by Django 3.1.7 on 2021-07-02 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 11, 54, 45, 834082)),
        ),
    ]
