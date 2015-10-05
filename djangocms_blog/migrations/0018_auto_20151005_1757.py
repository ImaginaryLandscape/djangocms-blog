# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0017_auto_20150824_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'ordering': ['sort_order'], 'verbose_name': 'blog category', 'verbose_name_plural': 'blog categories'},
        ),
        migrations.AlterModelOptions(
            name='newscategory',
            options={'ordering': ['sort_order'], 'verbose_name': 'news category', 'verbose_name_plural': 'news categories'},
        ),
    ]
