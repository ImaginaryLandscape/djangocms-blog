# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0010_blogcategory_sort_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='djangocms_blog.Post')),
            ],
            options={
                'ordering': ('-date_published', '-date_created'),
                'get_latest_by': 'date_published',
                'verbose_name': 'news article',
                'verbose_name_plural': 'news articles',
            },
            bases=('djangocms_blog.post',),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='blog_posts', verbose_name='category', to='djangocms_blog.BlogCategory', blank=True),
        ),
    ]
