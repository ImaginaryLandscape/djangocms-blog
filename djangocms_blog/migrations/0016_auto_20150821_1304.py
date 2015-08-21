# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
        ('djangocms_blog', '0015_post_related_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestpostsplugin',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='latestpostsplugin',
            name='tags',
        ),            
        migrations.CreateModel(
            name='LatestBlogPostsPlugin',
            fields=[
                ('latestpostsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='djangocms_blog.LatestPostsPlugin')),
                ('categories', models.ManyToManyField(help_text='Show only the blog articles tagged with chosen categories.', to='djangocms_blog.BlogCategory', verbose_name='filter by category', blank=True)),
                ('tags', taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='Show only the blog articles tagged with chosen tags.', verbose_name='filter by tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('djangocms_blog.latestpostsplugin',),
        ),
        migrations.CreateModel(
            name='LatestNewsPostsPlugin',
            fields=[
                ('latestpostsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='djangocms_blog.LatestPostsPlugin')),
                ('categories', models.ManyToManyField(help_text='Show only the news articles tagged with chosen categories.', to='djangocms_blog.NewsCategory', verbose_name='filter by category', blank=True)),
                ('tags', taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='Show only the blog articles tagged with chosen tags.', verbose_name='filter by tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('djangocms_blog.latestpostsplugin',),
        ),
        migrations.CreateModel(
            name='SelectNewsPostsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('posts', models.ManyToManyField(related_name='djangocms_news_posts_plugin', to='djangocms_blog.NewsPost')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
