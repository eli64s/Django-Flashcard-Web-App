# Generated by Django 2.1.5 on 2019-09-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0008_auto_20190928_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write_sentence',
            name='sentence',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]