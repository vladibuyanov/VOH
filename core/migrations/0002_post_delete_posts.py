# Generated by Django 4.1.2 on 2022-12-22 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('post', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2022, 12, 22, 14, 28, 16, 533103))),
            ],
            options={
                'verbose_name': 'Post',
            },
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
