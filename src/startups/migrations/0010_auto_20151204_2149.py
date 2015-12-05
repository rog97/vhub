# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0009_remove_startup_latest_funding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.TextField(default=False),
        ),
    ]
