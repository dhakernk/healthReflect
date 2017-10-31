# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topresultmapping',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='topresultmapping',
            name='resultType',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='topresulttype',
            name='resultId',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
