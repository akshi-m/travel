# Generated by Django 4.1.1 on 2022-09-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='traveldesk',
            name='number_of_person',
            field=models.IntegerField(default=1),
        ),
    ]
