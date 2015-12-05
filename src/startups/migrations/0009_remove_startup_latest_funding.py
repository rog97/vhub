# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0008_auto_20151203_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='latest_funding',
        ),
    ]
