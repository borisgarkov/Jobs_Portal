# Generated by Django 3.2.5 on 2022-04-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_auth', '0003_appbaseusermodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appbaseusermodel',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
