# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from blog import views as blogView

urlpatterns = [
    url(r'^category/(?P<category_id>.*)/(?P<page_num>\d*)/$', blogView.CategoryView.as_view(), name='category'),
    url(r'^category_date/(?P<year>\d+)/(?P<month>\d+)/(?P<page_num>\d*)/$', blogView.CategoryDateView.as_view(), name='category_date'),
    url(r'^article/(?P<article_id>.*)/$', blogView.ArticleView.as_view(), name='article'),
    url(r'^goodlink/(?P<category_id>.*)/(?P<page_num>\d*)/$', blogView.GoodlinkView.as_view(), name='goodlink'),
    url(r'^picture/(?P<category_id>.*)/(?P<page_num>\d*)/$', blogView.PictureView.as_view(), name='picture'),
    url(r'^comment/(?P<article_id>.*)/$', blogView.CommentView.as_view(), name='comment'),
    url(r'^contacts$', blogView.ContactsView.as_view(), name='contacts'),
    url(r'^about', blogView.AboutView.as_view(), name='about'),
]