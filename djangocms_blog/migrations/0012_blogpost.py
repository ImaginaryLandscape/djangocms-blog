# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0011_auto_20150819_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='djangocms_blog.Post')),
            ],
            options={
                'ordering': ('-date_published', '-date_created'),
                'get_latest_by': 'date_published',
                'verbose_name': 'blog article',
                'verbose_name_plural': 'blog articles',
            },
            bases=('djangocms_blog.post',),
        ),
    ]
