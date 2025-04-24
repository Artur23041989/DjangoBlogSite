from django import forms
from django.contrib.auth.models import User
from .models import Post

# 1 вариант создания формы
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label="Заголовок")
#     text = forms.CharField(widget=forms.Textarea, label="Текст поста")
#     author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
#     image = forms.ImageField(required=False, label="Изображение")



# 2 вариант создания формы
class PostForm(forms.ModelForm):
    # дополняем конструктор родительского класса
    def __init__(self, *args, **kwargs):
        # получаем author из именованных аргументов (его передали во views)
        author = kwargs.pop('author')
        # вызываем конструктор родительского
        super().__init__(*args, **kwargs)
        # устанавливаем начальное значение поля author
        self.fields['author'].initial = author
        # отключаем видимость этого поля в форме
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
       model = Post
       fields = ('title', 'text', 'image', 'author')

       labels = {
           'title': 'Заголовок',
           'text': 'Текст поста',
           'image': 'Изображение'
       }