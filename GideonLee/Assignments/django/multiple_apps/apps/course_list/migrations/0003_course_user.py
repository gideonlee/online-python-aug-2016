# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0002_auto_20160926_1934'),
        ('course_list', '0002_auto_20160924_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to='login_registration.User'),
        ),
    ]
