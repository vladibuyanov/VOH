# Generated by Django 4.1.2 on 2022-12-23 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_link_url_title_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(choices=[('Collaborative Divorce Resources', 'Collaborative Divorce Resources'), ('Collaborative Co-Parenting Mediation Resources', 'Collaborative Co-Parenting Mediation Resources'), ('Assessments and Screeners', 'Assessments and Screeners'), ('Consultation and Therapy Services', 'Consultation and Therapy Services'), ('Co-Parenting Mediation Program', 'Co-Parenting Mediation Program')], max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 14, 17, 18, 493001)),
        ),
    ]