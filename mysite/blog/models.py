# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', verbose_name=u"用户头像", max_length=200, blank=True, null=True)
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name=u'手机号码')
    url = models.URLField(max_length=200, blank=True, null=True, verbose_name=u'个人网址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name = verbose_name_plural = u"用户"
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'标签名称')

    class Meta:
        verbose_name = verbose_name_plural = u'标签'

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'分类名称')
    index = models.IntegerField(default=999, verbose_name=u'分类的排序')

    class Meta:
        verbose_name = verbose_name_plural = u'分类'
        ordering = ["index", "id"]

    def __unicode__(self):
        return self.name


class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        ret_date_list = []
        date_list = self.values('date_publish')

        for date in date_list:
            date1 = date['date_publish'].strftime('%Y/%m 文章存档')
            if date1 not in distinct_date_list:
                distinct_date_list.append(date1)
                count = self.filter(date_publish__month=6).count()
                ret_date_list.append({"date": date, "count": count})
                print date
                print count
                print date['date_publish'].year
                print date['date_publish'].month
                print "-------------------------"

        return ret_date_list



class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'文章标题')
    image = models.ImageField(verbose_name=u'文章图片', blank=True, null=True, upload_to='article', max_length=200)
    desc = models.CharField(max_length=50, verbose_name=u'文章描述')
    content = models.TextField(verbose_name=u'文章内容')
    click_count = models.IntegerField(default=0, verbose_name=u'点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name=u'是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    user = models.ForeignKey(User, verbose_name=u'文章作者')
    category = models.ForeignKey(Category, verbose_name=u'文章分类')
    tag = models.ManyToManyField(Tag, verbose_name=u'文章标签')

    objects = ArticleManager()

    class Meta:
        verbose_name = verbose_name_plural = u'文章'
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name=u'评论内容')
    username = models.CharField(max_length=100, verbose_name=u'用户名', blank=True, null=True)
    email = models.EmailField(max_length=100, verbose_name=u'邮箱地址', blank=True, null=True)
    url = models.URLField(max_length=100, verbose_name=u'个人网址', blank=True, null=True)
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    user = models.ForeignKey(User, verbose_name=u'用户', blank=True, null=True)
    article = models.ForeignKey(Article, verbose_name=u'文章', blank=True, null=True)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name=u'父级评论')

    class Meta:
        verbose_name = verbose_name_plural = u'评论'
        ordering = ['-date_publish', "-id"]

    def __unicode__(self):
        return str(self.content)


class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    description = models.CharField(max_length=200, verbose_name=u'友情链接描述')
    callback_url = models.URLField(verbose_name=u'url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    index = models.IntegerField(default=999, verbose_name=u'排序顺序(从小到大)')

    class Meta:
        verbose_name = verbose_name_plural = u'友情链接'
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'广告标题')
    description = models.CharField(max_length=200, verbose_name=u'广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name=u'广告图片')
    callback_url = models.URLField(null=True, blank=True, verbose_name=u'回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    index = models.IntegerField(default=999, verbose_name=u'排序顺序(从小到大)')

    class Meta:
        verbose_name = verbose_name_plural = u'广告'
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title


class GoodLink(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'链接标题')
    url = models.URLField(verbose_name=u'链接地址')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    category = models.ForeignKey(Category, verbose_name=u'链接分类', default=1)
    is_recommend = models.BooleanField(default=False, verbose_name=u'是否推荐')

    class Meta:
        verbose_name = verbose_name_plural = u'好的文章链接'
        ordering = ['-add_time']

    def __unicode__(self):
        return self.title


class PictureCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'分类名称')
    index = models.IntegerField(default=999, verbose_name=u'分类的排序')

    class Meta:
        verbose_name = verbose_name_plural = u'图片分类'
        ordering = ["index", "id"]

    def __unicode__(self):
        return self.name


class Pictures(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'图片标题', blank=True, null=True)
    image = models.ImageField(max_length=200, verbose_name=u'图片', upload_to='pictures')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    category = models.ForeignKey(PictureCategory, verbose_name=u'图片分类', default=1)

    class Meta:
        verbose_name = verbose_name_plural = u'图片'
        ordering = ['-add_time']

    def __unicode__(self):
        return self.title


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name=u'标题')
    name = models.CharField(max_length=50, verbose_name=u'名字', blank=True, null=True, )
    email = models.EmailField(max_length=100, verbose_name=u'邮箱地址', blank=True, null=True)
    content = models.TextField(max_length=1000, verbose_name=u'内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name=u'收到时间')

    class Meta:
        verbose_name = verbose_name_plural = u'消息'
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.subject


class MyProject(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'项目名称')
    cls = models.CharField(max_length=50, verbose_name=u'名字样式', default="", blank=True, null=True)
    title = models.TextField(max_length=500, verbose_name=u'项目介绍', default="", blank=True, null=True)
    desc = models.CharField(max_length=200, verbose_name=u'项目介绍')
    url = models.CharField(max_length=200, verbose_name=u'项目地址', default='#')
    index = models.IntegerField(default=999, verbose_name=u'排序（从大到小）')

    class Meta:
        verbose_name = verbose_name_plural = u'我的项目'
        ordering = ["-index", 'id']

    def __unicode__(self):
        return self.name
