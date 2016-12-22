# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0004_auto_20161126_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='drip',
            name='template_file',
            field=models.CharField(max_length=160, null=True, blank=True),
        ),
    ]
