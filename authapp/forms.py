#!/usr/bin/env python
# -*- coding: utf8 -*-

import re
import random, hashlib

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.core.validators import ValidationError

from .models import CustomerUser
from .models import CustomerUserProfile
from .models import Address


class CustomerUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'django-forms'


class CustomerUserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        user = super(CustomerUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
        user.save()

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'django-forms'
            field.help_text = ''
            self.fields['last_name'].label = 'Фамилия'
            self.fields['username'].label = 'Имя пользователя'
            self.fields['first_name'].label = 'Имя'
            self.fields['password1'].label = 'Придумайте пароль'
            self.fields['password2'].label = 'Повторите пароль'
            self.fields['email'].label = 'Почта'


class CustomerUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomerUserProfile
        fields = ('tag_line', 'about_me', 'gender')

    def __init__(self, *args, **kwargs):
        super(CustomerUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'edit-user-form-django'


class CustomerUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Email'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'edit-user-form-django'

    def clean_first_name(self):
        reg_exp = r'[А-я,-, ]+'

        data = self.cleaned_data['first_name']

        if re.match(reg_exp, data).group(0) != data:
            raise ValidationError('Имя должно состоять из русских букв')

        return data

    def clean_last_name(self):
        reg_exp = r'[А-я,-, ]+'

        data = self.cleaned_data['last_name']
        if re.match(reg_exp, data).group(0) != data:
            raise ValidationError('Фамилия должна состоять из русских букв')

        return data


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'address-form-django'
            if field_name in ['apartment', 'entrance', 'house', 'intercom']:
                field.widget.attrs['class'] += ' ten-long'
            if field_name == 'floor':
                field.widget.attrs['class'] += ' three-long'

    def clean_floor(self):
        reg_exp = r'[0-9,-]+'

        data = self.cleaned_data['floor']
        if data:
            try:
                if re.match(reg_exp, data).group(0) != data:
                    raise ValidationError('Этаж должен состоять из цифр')
            except AttributeError:
                raise ValidationError('Этаж должен состоять из цифр')

        return data

    def is_common_instance(self, form):
        if type(self) == type(form):
            return self.instance.id == form.instance.id
        else:
            raise TypeError('{} can\'t be equal {}'.format(type(self), type(form)))




