# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20170321_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='annotation',
            new_name='description',
        ),
    ]
