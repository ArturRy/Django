# Generated by Django 4.2.7 on 2023-11-11 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_scopes_alter_tag_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
    ]
