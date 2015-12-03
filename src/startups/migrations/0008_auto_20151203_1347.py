# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0007_auto_20151203_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
