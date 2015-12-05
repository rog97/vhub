# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0011_auto_20151204_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.TextField(),
        ),
    ]
