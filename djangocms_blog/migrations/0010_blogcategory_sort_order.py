# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0009_latestpostsplugin_tags_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='sort_order',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
