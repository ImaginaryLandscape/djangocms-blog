# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .feeds import LatestNewsEntriesFeed, TagFeed
from .views import (NewsPostArchiveView, NewsPostDetailView, NewsPostListView)

urlpatterns = patterns(
    '',
    url(r'^$', NewsPostListView.as_view(), name='newsposts-latest'),
    url(r'^feed/$', LatestNewsEntriesFeed(), name='newsposts-latest-feed'),
    url(r'^(?P<year>\d{4})/$', NewsPostArchiveView.as_view(), name='newsposts-archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', NewsPostArchiveView.as_view(), name='newsposts-archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$', NewsPostDetailView.as_view(), name='newspost-detail'),
)
