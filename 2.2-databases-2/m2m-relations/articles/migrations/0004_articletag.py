# Generated by Django 4.2.7 on 2023-11-10 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_rename_subjects_article_scopes"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="article_tag",
                        to="articles.article",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="article_tag",
                        to="articles.tag",
                    ),
                ),
            ],
        ),
    ]