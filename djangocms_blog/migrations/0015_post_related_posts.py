# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('djangocms_blog', '0014_selectpostsplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='related_posts',
            field=cms.models.fields.PlaceholderField(slotname=b'post_related_posts', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
