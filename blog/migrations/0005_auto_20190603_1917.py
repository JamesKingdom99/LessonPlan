# Generated by Django 2.2 on 2019-06-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190603_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postforms',
            name='presentation',
            field=models.SlugField(max_length=200),
        ),
    ]
