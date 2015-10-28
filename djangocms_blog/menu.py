# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.menu_bases import CMSAttachMenu
from django.db.models.signals import post_delete, post_save
from django.utils.translation import get_language, get_language_from_request, ugettext_lazy as _
from menus.base import Modifier, NavigationNode
from menus.menu_pool import menu_pool

from .models import BlogCategory, BlogPost, NewsCategory, NewsPost


class BlogCategoryMenu(CMSAttachMenu):
    name = _('Blog Category menu')

    def get_nodes(self, request):        
        nodes = []

        language = get_language_from_request(request, check_path=True)        

        categories = BlogCategory.objects.active_translations(language).distinct()        
        categories = categories.order_by('parent__id', 'sort_order', 'id', 'translations__name')
        for category in categories:
            node = NavigationNode(
                category.name,
                category.get_absolute_url(),
                '%s-%s' % (category.__class__.__name__, category.pk),
                ('%s-%s' % (category.__class__.__name__, category.parent.id) if category.parent
                else None),
                attr=dict(posts=category.blog_posts.published(),),
            )
            nodes.append(node)

        return nodes

menu_pool.register_menu(BlogCategoryMenu)

class NewsCategoryMenu(CMSAttachMenu):
    name = _('News Category menu')

    def get_nodes(self, request):
        nodes = []
        qs = NewsCategory.objects.translated(get_language())
        qs = qs.order_by('sort_order', 'id', 'translations__name')
        for category in qs:
            node = NavigationNode(
                category.name,
                category.get_absolute_url(),
                category.pk,
                attr=dict(posts=category.news_posts.published(),),                
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(NewsCategoryMenu)


class BlogNavModifier(Modifier):
    """
    This navigation modifier makes sure that when
    a particular blog post is viewed,
    a corresponding category is selected in menu
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        if not hasattr(request, 'toolbar'):
            return nodes
        models = ('djangocms_blog.blogpost', 'djangocms_blog.blogcategory')
        model = request.toolbar.get_object_model()
        if model not in models:
            return nodes
        if model == 'djangocms_blog.blogcategory':
            cat = request.toolbar.obj
        else:
            cat = request.toolbar.obj.categories.first()
        if not cat:
            return nodes

        for node in nodes:
            if (node.namespace.startswith(BlogCategoryMenu.__name__) and
                    cat.pk == node.id):
                node.selected = True
                # no break here because django-cms maintains two menu structures
                # for every apphook (attached to published page and draft page)
        return nodes

menu_pool.register_modifier(BlogNavModifier)

class NewsNavModifier(Modifier):
    """
    This navigation modifier makes sure that when
    a particular blog post is viewed,
    a corresponding category is selected in menu
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        if not hasattr(request, 'toolbar'):
            return nodes
        models = ('djangocms_blog.newspost', 'djangocms_blog.newscategory')
        model = request.toolbar.get_object_model()
        if model not in models:
            return nodes
        if model == 'djangocms_blog.newscategory':
            cat = request.toolbar.obj
        else:
            cat = request.toolbar.obj.categories.first()
        if not cat:
            return nodes

        for node in nodes:
            if (node.namespace.startswith(NewsCategoryMenu.__name__) and
                    cat.pk == node.id):
                node.selected = True
                # no break here because django-cms maintains two menu structures
                # for every apphook (attached to published page and draft page)
        return nodes

menu_pool.register_modifier(NewsNavModifier)


def clear_menu_cache(**kwargs):
    menu_pool.clear(all=True)

post_save.connect(clear_menu_cache, sender=BlogCategory)
post_delete.connect(clear_menu_cache, sender=BlogCategory)
post_save.connect(clear_menu_cache, sender=NewsCategory)
post_delete.connect(clear_menu_cache, sender=NewsCategory)
