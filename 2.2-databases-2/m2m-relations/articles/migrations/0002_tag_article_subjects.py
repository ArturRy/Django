# Generated by Django 4.2.7 on 2023-11-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Тематика')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='subjects',
            field=models.ManyToManyField(related_name='articles', to='articles.tag'),
        ),
    ]
