# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('djangocms_blog', '0018_auto_20151005_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='related_posts',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=cms.models.fields.PlaceholderField(related_name='blog_post_content', slotname='post_content', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='related_posts',
            field=cms.models.fields.PlaceholderField(related_name='blog_post_related_posts', slotname='post_related_posts', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='newspost',
            name='content',
            field=cms.models.fields.PlaceholderField(related_name='news_post_content', slotname='post_content', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='newspost',
            name='related_posts',
            field=cms.models.fields.PlaceholderField(related_name='news_post_related_posts', slotname='post_related_posts', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='abstract',
            field=djangocms_text_ckeditor.fields.HTMLField(default='', verbose_name='abstract', blank=True),
        ),
    ]
