from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, NewRegistrationForm


def register(request):
    # когда отправляем заполненную форму на сервер
    if request.method == 'POST':
        form = NewRegistrationForm(request.POST)
        # если форма валидна
        if form.is_valid():
            # создаем объект пользователя без записи в базу данных
            new_user = form.save(commit=False)
            # хэшируем пароль при помощи set_password
            new_user.set_password(form.cleaned_data['password'])
            # сохпаняем пользователя в БД
            new_user.save()
            context = {"title": "Регистрация завершена", "new_user": new_user}
            return render(request, template_name="users/registration_done.html", context=context)
    # если метод GET (страница с пустой формой регистрации)
    form = NewRegistrationForm()
    context = {"title": "Регистрация пользователя", "register_form": form}
    return render(request, template_name="users/registration.html", context=context)

def log_in(request):
    pass

def log_out(request):
    pass

def user_profile(request, pk):
    pass