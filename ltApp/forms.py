# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from ltApp.models import UserLt
from django.core.validators import RegexValidator


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='username',
                               min_length=5,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
                               )

    first_name = forms.CharField(label='Nombre',
                                 min_length=5,
                                 widget=forms.TextInput(attrs={'placeholder': 'Nombre'}),
                                 )
    last_name = forms.CharField(label='Apellido',
                                min_length=5,
                                widget=forms.TextInput(attrs={'placeholder': 'Apellido'}),
                                )
    email = forms.EmailField(label='username',
                             min_length=5,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}),
                             )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserLtForm(forms.ModelForm):
    address = forms.CharField(label='Dirección',
                              min_length=5,
                              widget=forms.TextInput(attrs={'placeholder': 'Dirección'}),
                              )
    city = forms.CharField(label='Ciudad',
                           min_length=5,
                           widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}),
                           )
    commune = forms.CharField(label='Comuna',
                              min_length=5,
                              widget=forms.TextInput(attrs={'placeholder': 'Comuna'}),
                              )
    rut = forms.CharField(label='Rut',
                          min_length=5,
                          widget=forms.TextInput(attrs={'placeholder': 'Rut'}),
                          )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="El numero ingresado no es del formato: '+999999999' o no esta entre 9 y 15 digitos.")
    phone = forms.CharField(validators=[phone_regex], label='Telefono', widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}),)

    class Meta:
        model = UserLt
        fields = ('address', 'phone', 'rut', 'city', 'commune')
