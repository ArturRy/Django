# Generated by Django 4.2.7 on 2023-11-13 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0011_alter_tag_subject"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Раздел", "verbose_name_plural": "Разделы"},
        ),
        migrations.AddField(
            model_name="tag",
            name="article",
            field=models.ManyToManyField(
                related_name="tag", through="articles.ArticleTag", to="articles.article"
            ),
        ),
        migrations.AlterField(
            model_name="articletag",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
            ),
        ),
        migrations.AlterField(
            model_name="articletag",
            name="is_main",
            field=models.BooleanField(),
        ),
    ]