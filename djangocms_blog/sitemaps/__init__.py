# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib.sitemaps import Sitemap

from ..models import BlogPost, NewsPost, BlogCategory, NewsCategory

class BlogCategorySitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return BlogCategory.objects.all()

    def lastmod(self, obj):
        return obj.date_modified

class BlogPostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return BlogPost.objects.published()

    def lastmod(self, obj):
        return obj.date_modified

class NewsPostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return NewsPost.objects.published()

    def lastmod(self, obj):
        return obj.date_modified
