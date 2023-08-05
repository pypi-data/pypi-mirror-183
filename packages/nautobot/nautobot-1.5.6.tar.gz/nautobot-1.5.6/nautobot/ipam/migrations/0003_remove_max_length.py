# Generated by Django 3.1.8 on 2021-05-14 19:58

from django.db import migrations
import nautobot.ipam.fields


class Migration(migrations.Migration):

    dependencies = [
        ("ipam", "0002_initial_part_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aggregate",
            name="broadcast",
            field=nautobot.ipam.fields.VarbinaryIPField(db_index=True),
        ),
        migrations.AlterField(
            model_name="aggregate",
            name="network",
            field=nautobot.ipam.fields.VarbinaryIPField(db_index=True),
        ),
        migrations.AlterField(
            model_name="ipaddress",
            name="broadcast",
            field=nautobot.ipam.fields.VarbinaryIPField(db_index=True),
        ),
        migrations.AlterField(
            model_name="ipaddress",
            name="host",
            field=nautobot.ipam.fields.VarbinaryIPField(db_index=True),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="broadcast",
            field=nautobot.ipam.fields.VarbinaryIPField(db_index=True),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="network",
            field=nautobot.ipam.fields.VarbinaryIPField(db_index=True),
        ),
    ]
