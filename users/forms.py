from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите логин',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'form-control',
        'placeholder': 'Введите пароль',
    }))


    class Meta:
        model = User
        fields = ('username', 'password')



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите логин'
    }))

    nickname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите никнейм'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль еще раз'
    }))


    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'password1', 'password2')



class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'class': 'form-control'
    }))

    nickname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input nickname'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'readonly': True,
        'class': 'form-control'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose image'
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'image')