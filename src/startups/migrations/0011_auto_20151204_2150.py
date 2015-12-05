# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0010_auto_20151204_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.TextField(default='Enter a 1-line description here'),
        ),
    ]
