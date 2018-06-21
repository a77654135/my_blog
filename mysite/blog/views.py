# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.conf import settings
from blog.models import *
from blog.models import Message as ModelMessage
from blog.forms import Message as FormMessage
from blog.forms import Comment as FormComment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.http import Http404,HttpResponseRedirect
import markdown

import logging

# Create your views here.


logger = logging.getLogger(__name__)


def page_not_found(request):
    return render(request, 'blog/404.html')


def global_settings(request):
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    SITE_SOCIALS = settings.SITE_SOCIALS
    SITE_STYLEBAR = settings.SITE_STYLEBAR
    SITE_TOP_NAV = settings.SITE_TOP_NAV

    category_list = Category.objects.all()
    picture_category_list = PictureCategory.objects.all()

    return locals()


class IndexView(View):

    def get(self, request):
        return render(request, 'blog/index.html')


class CategoryView(View):

    def get(self, request, category_id, page_num=1):
        try:
            page_num = int(page_num)
            category_id = int(category_id)
        except ValueError,e:
            page_num = 1
            category_id = 0
        except Exception, e:
            page_num = 1
            category_id = 0

        if category_id == 0:
            category_name = u"全部"
            article_list = Article.objects.all()
        else:
            category = get_object_or_404(Category, pk=category_id)
            category_name = category.name
            article_list = Article.objects.filter(category=category)

        paginator = Paginator(article_list, settings.CATEGORY_PER_PAGE)
        try:
            articles = paginator.page(page_num)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)

        return render(request, 'blog/blog.html', {'articles': articles, 'category_id': category_id, 'category_name': category_name})

class ArticleView(View):

    def get(self, request, article_id):
        try:
            article_id = int(article_id)
        except:
            article_id = 1

        article = get_object_or_404(Article, pk=article_id)
        article.content = markdown.markdown(article.content, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
        comments = article.comment_set.all()
        return render(request, 'blog/article.html', {"article": article, "comments": comments})


class GoodlinkView(View):

    def get(self, request, category_id, page_num):
        try:
            category_id = int(category_id)
            page_num = int(page_num)
        except:
            category_id = 0
            page_num = 1

        if category_id == 0:
            category_name = u"全部"
            goodlink_list = GoodLink.objects.all()
        else:
            category = get_object_or_404(Category, pk=category_id)
            category_name = category.name
            goodlink_list = GoodLink.objects.filter(category=category)

        paginator = Paginator(goodlink_list, settings.GOODLINK_PER_PAGE)
        try:
            goodlinks = paginator.page(page_num)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            goodlinks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            goodlinks = paginator.page(paginator.num_pages)

        return render(request, 'blog/goodlink.html', {'goodlinks': goodlinks, 'category_id': category_id, "category_name": category_name})


class PictureView(View):
    def get(self, request, category_id, page_num):
        try:
            category_id = int(category_id)
            page_num = int(page_num)
        except:
            category_id = 0
            page_num = 1

        if category_id == 0:
            category_name = u"全部"
            picture_list = Pictures.objects.all()
        else:
            category = get_object_or_404(PictureCategory, pk=category_id)
            category_name = category.name
            picture_list = Pictures.objects.filter(category=category)

        paginator = Paginator(picture_list, settings.PICTURE_PER_PAGE)
        try:
            pictures = paginator.page(page_num)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            pictures = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            pictures = paginator.page(paginator.num_pages)

        return render(request, 'blog/gallery.html', {'pictures': pictures, 'category_id': category_id, "category_name": category_name})

class ContactsView(View):
    def get(self, request):
        return render(request, 'blog/contacts.html')

    def post(self, request):
        form = FormMessage(request.POST)
        if form.is_valid():
            ModelMessage.objects.create(subject=form.cleaned_data["subject"], name=form.cleaned_data["name"], email=form.cleaned_data["email"], content=form.cleaned_data["content"])

        return render(request, 'blog/contacts.html', {'error': form.errors})

class AboutView(View):
    def get(self, request):
        my_proj = MyProject.objects.all()
        return render(request, 'blog/about.html', {'my_proj': my_proj})

class CommentView(View):
    def post(self, request, article_id):
        print "article_id:   {}".format(article_id)
        try:
            article_id = int(article_id)
        except ValueError:
            article_id = 1
        form = FormComment(request.POST)
        if form.is_valid():
            article = get_object_or_404(Article, pk=article_id)
            username=form.cleaned_data["username"]
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist,MultipleObjectsReturned:
                user = None
            except Exception,e:
                user = None
            Comment.objects.create(
                username=username,
                email=form.cleaned_data["email"],
                url=form.cleaned_data["url"],
                content=form.cleaned_data["content"],
                article=article,
                user=user,
            )
        return HttpResponseRedirect(reverse('article', args=(article_id,)))


