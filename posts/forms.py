'''
Created on Dec 23, 2017

@author: S528358
'''
from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'content']