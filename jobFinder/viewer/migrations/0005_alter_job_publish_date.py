# Generated by Django 3.2.5 on 2021-07-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_remove_job_active_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
