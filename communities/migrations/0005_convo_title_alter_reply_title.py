# Generated by Django 5.1.7 on 2025-04-21 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("communities", "0004_remove_convo_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="convo",
            name="title",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="reply",
            name="title",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
