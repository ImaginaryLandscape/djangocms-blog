# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0007_auto_20150719_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='sort_order',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
