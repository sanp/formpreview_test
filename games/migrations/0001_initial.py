# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=200, verbose_name=b'Location')),
                ('game', models.IntegerField(default=0, choices=[(0, b'Football'), (1, b'Basketball'), (2, b'Tennis'), (3, b'Other')])),
                ('game_date', models.DateField(verbose_name=b'Game Date')),
            ],
        ),
    ]
