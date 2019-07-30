# Generated by Django 2.2 on 2019-06-04 01:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_board_thinker'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=1, verbose_name='Content'),
            preserve_default=False,
        ),
    ]
