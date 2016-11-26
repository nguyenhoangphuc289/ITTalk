# -*- coding: utf-8 -*
from django.db import models
from django import forms
from redactor.widgets import RedactorEditor


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeHolder': 'Tiêu đề...',
        'class': 'form-control'
    }))
    content = forms.CharField(widget=RedactorEditor(attrs={
        'placeHolder': 'Bạn muốn chia sẻ gì...',
    }))
