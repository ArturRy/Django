# Generated by Django 4.2.7 on 2023-11-11 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_articletag_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
    ]
