from django import forms
from django.contrib.auth.models import User
from .models import Post

# 1 вариант создания формы
class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label="Заголовок")
    text = forms.CharField(widget=forms.Textarea, label="Текст поста")
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")

# 2 вариант создания формы
# class NewPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'text')
#
#         lables = {
#             'title': 'Заголовок',
#             'text': 'Текст поста'
#         }