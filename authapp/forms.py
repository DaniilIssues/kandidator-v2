from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from authapp.models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'telephone_num')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['username'].widget = forms.EmailInput()
        self.fields['username'].widget.attrs.update({'placeholder': 'Введите email.'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Введите пароль.'})
        self.fields['telephone_num'].widget.attrs.update({'placeholder': 'Введите номер телефона'})
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form__input'


class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Введите email.'})
        self.fields['password'].widget.attrs.update({'placeholder': '*****************'})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form__input'
