# -*- coding: utf-8 -*-

from django import forms


class Message(forms.Form):
    subject = forms.CharField(max_length=200, required=True, error_messages={
        "required": "主题不能为空"
    })
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=100, required=False)
    content = forms.CharField(max_length=1000, required=True, error_messages={
        "required": "内容不能为空"
    })

class Comment(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=100, required=False)
    url = forms.URLField(max_length=100, required=False)
    content = forms.CharField(max_length=500, required=True, error_messages={
        "required": "内容不能为空"
    })