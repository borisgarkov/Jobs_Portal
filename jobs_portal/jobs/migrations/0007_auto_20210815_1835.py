# Generated by Django 3.2.5 on 2021-08-15 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_jobmodel_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
