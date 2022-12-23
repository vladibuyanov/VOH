# Generated by Django 4.1.2 on 2022-12-23 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_delete_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Collaborative Divorce Resources', 'Collaborative Divorce Resources'), ('Collaborative Co-Parenting Mediation Resources', 'Collaborative Co-Parenting Mediation Resources'), ('Assessments & Screeners', 'Assessments & Screeners'), ('Consultation & Therapy Services', 'Consultation & Therapy Services'), ('Co-Parenting Mediation Program', 'Co-Parenting Mediation Program')], max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Link',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 13, 46, 15, 997651)),
        ),
    ]
