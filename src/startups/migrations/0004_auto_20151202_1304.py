# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0003_auto_20151202_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='description',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='founders',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='investors',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='latest_funding',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='total_funding',
        ),
    ]
