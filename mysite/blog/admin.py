# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from models import *
from django import forms
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'category', 'date_publish')
    list_display_links = ('title', 'desc')
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
    fieldsets = (
        ('基础信息', {
            'fields': ('title', 'desc', 'content', 'image', 'user', 'tag', 'category')
        }),
        ('高级设置', {
            'fields': ('is_recommend',)
        })
    )

    # class Media:
    #     js = (
    #         '/static/js/kindeditor/kindeditor-all-min.js',
    #         '/static/js/kindeditor/lang/zh-CN.js',
    #         '/static/js/kindeditor/config.js',
    #     )


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'qq', 'mobile', 'email')
    search_fields = ('username', 'qq', 'mobile', 'email')


class GoodlinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_recommend')
    list_display_links = ('title', 'url')
    search_fields = ('title', 'url')
    list_editable = ('is_recommend',)


class PictureForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = ('title', 'image', 'category')
        widgets = {
            'image': forms.FileInput(attrs={
                'multiple': True
            })
        }


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('title', "image")
    form = PictureForm


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email')
    list_display_links = ('subject', 'name', 'email')
    readonly_fields = ('subject', 'name', 'email', 'content')


class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'url', 'index')
    list_display_links = ('name', 'desc', 'url')
    search_fields = ('name', 'desc')
    list_editable = ('index',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'email', 'date_publish')
    search_fields = ('username', 'content', 'email')
    fields = ('username', 'content', 'email')


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad)
admin.site.register(Message, MessageAdmin)
admin.site.register(GoodLink, GoodlinkAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Pictures, PicturesAdmin)
admin.site.register(PictureCategory)
admin.site.register(MyProject, MyProjectAdmin)
