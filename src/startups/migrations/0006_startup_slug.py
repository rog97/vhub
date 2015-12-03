# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0005_auto_20151202_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='slug',
            field=models.SlugField(default='slug-field'),
        ),
    ]
