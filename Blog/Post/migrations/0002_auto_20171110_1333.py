# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/img/blog_img/'),
        ),
    ]
