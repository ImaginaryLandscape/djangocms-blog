# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django import forms

from .forms import LatestEntriesForm, SelectPostsForm
from .models import AuthorEntriesPlugin, BlogCategory, NewsCategory, LatestBlogPostsPlugin, LatestNewsPostsPlugin, Post, BlogPost, NewsPost, SelectPostsPlugin, SelectNewsPostsPlugin
from .settings import get_setting


class BlogPlugin(CMSPluginBase):
    module = 'Blog'


class BlogLatestEntriesPlugin(BlogPlugin):
    """
    Cached plugin which returns the latest published posts
    """
    render_template = 'djangocms_blog/plugins/latest_entries.html'
    name = _('Latest Blog Articles')
    model = LatestBlogPostsPlugin
    form = LatestEntriesForm
    filter_horizontal = ('categories',)
    fields = ('latest_posts', 'tags', 'categories')

    def render(self, context, instance, placeholder):
        context = super(BlogLatestEntriesPlugin, self).render(context, instance, placeholder)
        try:
            context['posts_list'] = instance.get_posts(context['request'])
        except:
            pass
        context['TRUNCWORDS_COUNT'] = get_setting('POSTS_LIST_TRUNCWORDS_COUNT')
        return context

class NewsLatestEntriesPlugin(BlogLatestEntriesPlugin):
    name = _('Latest News Articles')
    model = LatestNewsPostsPlugin

    def render(self, context, instance, placeholder):
        context = super(NewsLatestEntriesPlugin, self).render(context, instance, placeholder)
        try:
            context['posts_list'] = instance.get_posts(context['request'])
        except:
            pass
        context['TRUNCWORDS_COUNT'] = get_setting('POSTS_LIST_TRUNCWORDS_COUNT')
        return context

class BlogLatestEntriesPluginUnCached(BlogLatestEntriesPlugin):
    """
    Non cached plugin which returns the latest posts taking into account the
      user / toolbar state
    """
    name = _('Latest Blog Articles (uncached)')
    cache = False


class BlogAuthorPostsPlugin(BlogPlugin):
    module = _('Blog')
    name = _('Author Blog Articles')
    model = AuthorEntriesPlugin
    form = LatestEntriesForm
    render_template = 'djangocms_blog/plugins/authors.html'
    filter_horizontal = ['authors']

    def render(self, context, instance, placeholder):
        context = super(BlogAuthorPostsPlugin, self).render(context, instance, placeholder)
        context['authors_list'] = instance.get_authors()
        return context


class BlogTagsPlugin(BlogPlugin):
    module = _('Blog')
    name = _('Tags')
    model = CMSPlugin
    render_template = 'djangocms_blog/plugins/tags.html'

    def render(self, context, instance, placeholder):
        context = super(BlogTagsPlugin, self).render(context, instance, placeholder)
        context['tags'] = Post.objects.tag_cloud(queryset=Post.objects.published())
        return context


class BlogCategoryPlugin(BlogPlugin):
    module = _('Blog')
    name = _('Blog Categories')
    model = CMSPlugin
    render_template = 'djangocms_blog/plugins/categories.html'

    def render(self, context, instance, placeholder):
        context = super(BlogCategoryPlugin, self).render(context, instance, placeholder)
        context['categories'] = BlogCategory.objects.all()
        return context

class NewsCategoryPlugin(BlogCategoryPlugin):
    name = _('News Categories')

    def render(self, context, instance, placeholder):
        context = super(NewsCategoryPlugin, self).render(context, instance, placeholder)
        context['categories'] = NewsCategory.objects.all()
        return context


class BlogArchivePlugin(BlogPlugin):
    module = _('Blog')
    name = _('BlogArchive')
    model = CMSPlugin
    render_template = 'djangocms_blog/plugins/archive.html'

    def render(self, context, instance, placeholder):
        context = super(BlogArchivePlugin, self).render(context, instance, placeholder)
        context['dates'] = BlogPost.objects.get_months(queryset=BlogPost.objects.published())
        return context

class NewsArchivePlugin(BlogArchivePlugin):
    name = _('News Archive')
    render_template = 'djangocms_blog/plugins/newsarchive.html'

    def render(self, context, instance, placeholder):
        context = super(NewsArchivePlugin, self).render(context, instance, placeholder)
        context['dates'] = NewsPost.objects.get_months(queryset=NewsPost.objects.published())
        return context

class BlogSelectPostsPlugin(BlogPlugin):
    module = _('Blog')
    filter_horizontal = ('posts',)
    form = SelectPostsForm
    name = _('Select Blog Articles')
    model = SelectPostsPlugin
    render_template = 'djangocms_blog/plugins/posts.html'

    def render(self, context, instance, placeholder):
        context['posts'] = instance.posts.all()
        return context

class NewsSelectPostsPlugin(BlogSelectPostsPlugin):
    model = SelectNewsPostsPlugin
    name = _('Select News Articles')

plugin_pool.register_plugin(BlogLatestEntriesPlugin)
plugin_pool.register_plugin(NewsLatestEntriesPlugin)
#plugin_pool.register_plugin(BlogLatestEntriesPluginUnCached)
plugin_pool.register_plugin(BlogAuthorPostsPlugin)
plugin_pool.register_plugin(BlogTagsPlugin)
plugin_pool.register_plugin(BlogArchivePlugin)
plugin_pool.register_plugin(NewsArchivePlugin)
plugin_pool.register_plugin(BlogCategoryPlugin)
plugin_pool.register_plugin(NewsCategoryPlugin)
plugin_pool.register_plugin(BlogSelectPostsPlugin)
plugin_pool.register_plugin(NewsSelectPostsPlugin)
