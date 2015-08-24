# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import cms.models.fields
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0012_auto_20150607_2207'),
        ('djangocms_blog', '0016_auto_20150821_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='content',
            field=cms.models.fields.PlaceholderField(related_name='blogcategory_content', slotname=b'category_content', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='header_image',
            field=filer.fields.image.FilerImageField(related_name='blogcategory_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='header image', blank=True, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='intro',
            field=cms.models.fields.PlaceholderField(related_name='blogcategory_intro', slotname=b'category_intro', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='abstract',
            field=djangocms_text_ckeditor.fields.HTMLField(default=b'', verbose_name='teaser', blank=True),
        ),
    ]
