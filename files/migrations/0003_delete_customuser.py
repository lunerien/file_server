# Generated by Django 5.0 on 2023-12-16 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0002_customuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
