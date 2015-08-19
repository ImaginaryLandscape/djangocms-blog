# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0012_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'verbose_name': 'news category',
                'verbose_name_plural': 'news categories',
            },
        ),
        migrations.CreateModel(
            name='NewsCategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(verbose_name='slug', blank=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='djangocms_blog.NewsCategory', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'djangocms_blog_newscategory_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'news category Translation',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(related_name='blog_posts', verbose_name='category', to='djangocms_blog.BlogCategory'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='categories',
            field=models.ManyToManyField(related_name='news_posts', verbose_name='category', to='djangocms_blog.NewsCategory', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='newscategorytranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
