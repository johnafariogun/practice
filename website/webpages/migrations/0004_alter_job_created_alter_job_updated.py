# Generated by Django 4.0.6 on 2022-07-19 15:58

from django.db import migrations, models
import django.utils.timezone
import webpages.models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_alter_job_created_alter_job_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
       
    ]