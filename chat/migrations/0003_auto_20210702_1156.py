# Generated by Django 3.1.7 on 2021-07-02 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210702_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
