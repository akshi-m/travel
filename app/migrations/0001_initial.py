# Generated by Django 4.1.1 on 2022-09-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('timing', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Locations',
                'db_table': 'locations',
                'ordering': ('category',),
            },
        ),
    ]