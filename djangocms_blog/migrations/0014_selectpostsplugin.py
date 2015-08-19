# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('djangocms_blog', '0013_auto_20150819_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectPostsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('posts', models.ManyToManyField(related_name='djangocms_blog_posts_plugin', to='djangocms_blog.BlogPost')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
