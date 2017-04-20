# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20170322_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='photo',
            field=models.ImageField(verbose_name='Плашка', blank=True, upload_to='uploads/'),
        ),
    ]
