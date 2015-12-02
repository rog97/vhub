# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='description',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='startup',
            name='founders',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='startup',
            name='investors',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='startup',
            name='latest_funding',
            field=models.DecimalField(max_digits=50, default='-', decimal_places=1),
        ),
        migrations.AddField(
            model_name='startup',
            name='total_funding',
            field=models.DecimalField(max_digits=50, default='-', decimal_places=1),
        ),
    ]
