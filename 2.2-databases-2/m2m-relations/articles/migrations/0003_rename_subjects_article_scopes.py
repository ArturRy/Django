# Generated by Django 4.2.7 on 2023-11-08 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_tag_article_subjects"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="subjects",
            new_name="scopes",
        ),
    ]