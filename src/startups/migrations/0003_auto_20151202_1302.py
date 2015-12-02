# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_auto_20151202_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='latest_funding',
            field=models.DecimalField(default=0, max_digits=50, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='startup',
            name='total_funding',
            field=models.DecimalField(default=0, max_digits=50, decimal_places=1),
        ),
    ]
