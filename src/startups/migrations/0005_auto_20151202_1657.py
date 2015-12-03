# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0004_auto_20151202_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='description',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='latest_funding',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=50),
        ),
    ]
