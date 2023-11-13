# Generated by Django 4.2.7 on 2023-11-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0004_articletag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="scopes",
        ),
        migrations.AddField(
            model_name="tag",
            name="scopes",
            field=models.ManyToManyField(related_name="scopes", to="articles.article"),
        ),
    ]