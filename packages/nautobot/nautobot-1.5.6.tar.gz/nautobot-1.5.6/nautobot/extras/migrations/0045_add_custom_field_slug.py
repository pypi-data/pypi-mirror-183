# Generated by Django 3.2.14 on 2022-08-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0044_add_job_hook"),
    ]

    operations = [
        migrations.AddField(
            model_name="customfield",
            name="slug",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
