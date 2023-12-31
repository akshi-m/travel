# Generated by Django 4.1.1 on 2022-09-07 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_locations_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('review', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='images')),
                ('date_generated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Traveldesk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('expected_date', models.DateField()),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField(max_length=1000)),
                ('number_of_person', models.IntegerField()),
                ('date_generated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'traveldesk',
            },
        ),
    ]
