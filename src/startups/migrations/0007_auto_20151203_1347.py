# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0006_startup_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='slug',
            field=models.SlugField(),
        ),
    ]
