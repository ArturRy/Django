# Generated by Django 4.2.7 on 2023-11-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0010_remove_article_scopes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="subject",
            field=models.CharField(max_length=200, verbose_name="name"),
        ),
    ]
