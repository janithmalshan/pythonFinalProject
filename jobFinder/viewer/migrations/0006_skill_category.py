# Generated by Django 3.2.5 on 2021-07-24 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_alter_job_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.category'),
        ),
    ]
