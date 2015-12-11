# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from copy import deepcopy

from cms.admin.placeholderadmin import FrontendEditableAdminMixin, PlaceholderAdminMixin
from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from parler.admin import TranslatableAdmin

from .models import BlogCategory, NewsCategory, BlogPost, NewsPost
from .settings import get_setting

try:
    from admin_enhancer.admin import EnhancedModelAdminMixin
except ImportError:
    class EnhancedModelAdminMixin(object):
        pass


class BlogCategoryAdmin(EnhancedModelAdminMixin, FrontendEditableAdminMixin,
                        PlaceholderAdminMixin, TranslatableAdmin):
    list_display = ['name', 'parent', 'sort_order']
    list_editable = ['sort_order']
    list_filter = ['parent']
    enhance_exclude = ('header_image')    

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

    class Meta:
        ordering = ('parent', 'sort_order', 'name')

    class Media:
        css = {
            'all': ('%sdjangocms_blog/css/%s' % (settings.STATIC_URL,
                                                 'djangocms_blog_admin.css'),)
        }

class NewsCategoryAdmin(BlogCategoryAdmin):
    list_display = ['name', 'sort_order']
    list_filter = []

    class Meta:
        ordering = ('sort_order', 'name')

class PostAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                TranslatableAdmin, EnhancedModelAdminMixin):
    list_display = ['title', 'author', 'get_categories', 'date_published']
    list_filter = ['categories']
    list_per_page = 50
    search_fields = ('translations__title',)
    date_hierarchy = 'date_published'
    raw_id_fields = ['author']
    frontend_editable_fields = ('title', 'abstract', 'post_text')
    enhance_exclude = ('main_image', 'tags')
    _fieldsets = [
        (None, {
            'fields': [('title', 'categories')]
        }),
        ('Info', {
            'fields': (['slug', 'tags'],
                       ('date_published', 'date_published_end', 'enable_comments')),
            'classes': ('collapse',)
        }),
        ('Images', {
            'fields': (('main_image', 'main_image_thumbnail', 'main_image_full'),),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': [('meta_description', 'meta_title', 'meta_keywords')],
            'classes': ('collapse',)
        }),
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'meta_description':
            original_attrs = field.widget.attrs
            original_attrs['maxlength'] = 160
            field.widget = forms.TextInput(original_attrs)
        elif db_field.name == 'meta_title':
            field.max_length = 70
        return field

    def get_fieldsets(self, request, obj=None):
        fsets = deepcopy(self._fieldsets)
    
        if request.user.has_perm('djangocms_blog.can_publish_blog'):
            fsets[0][1]['fields'].append('publish')
        if self.use_abstract():
            fsets[0][1]['fields'].append('abstract')
        if not get_setting('USE_PLACEHOLDER'):
            fsets[0][1]['fields'].append('post_text')
        if get_setting('MULTISITE'):
            fsets[1][1]['fields'][0].append('sites')
        if request.user.is_superuser:
            fsets[1][1]['fields'][0].append('author')
        return fsets

    def get_categories(self, obj):
        return ",<br>".join([p.name for p in obj.categories.all()])
    get_categories.short_description = 'Categories'
    get_categories.allow_tags = True

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not obj.author_id and get_setting('AUTHOR_DEFAULT'):
            if get_setting('AUTHOR_DEFAULT') is True:
                user = request.user
            else:
                user = get_user_model().objects.get(username=get_setting('AUTHOR_DEFAULT'))
            obj.author = user
        super(PostAdmin, self).save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ('%sdjangocms_blog/css/%s' % (settings.STATIC_URL,
                                                 'djangocms_blog_admin.css'),)
        }

class BlogPostAdmin(PostAdmin):
    def use_abstract(self):
        return get_setting('USE_ABSTRACT')
            

class NewsPostAdmin(PostAdmin):
    def use_abstract(self):
        return get_setting('NEWS_USE_ABSTRACT')

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(NewsPost, NewsPostAdmin)
