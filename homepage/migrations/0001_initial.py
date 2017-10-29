# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopResultMapping',
            fields=[
                ('id', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('resultType', models.IntegerField(max_length=5)),
                ('resultName', models.CharField(max_length=250, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopResultType',
            fields=[
                ('resultId', models.IntegerField(max_length=5, serialize=False, primary_key=True)),
                ('resultTopic', models.CharField(max_length=250)),
            ],
        ),
    ]
