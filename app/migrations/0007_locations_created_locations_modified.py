# Generated by Django 4.1.1 on 2022-09-12 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_feedback_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 12, 48, 12, 709023)),
        ),
        migrations.AddField(
            model_name='locations',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
