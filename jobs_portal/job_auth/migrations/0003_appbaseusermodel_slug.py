# Generated by Django 3.2.5 on 2022-04-02 14:12

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job_auth', '0002_alter_appbaseusermodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='appbaseusermodel',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='username'),
        ),
    ]