import re

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from authapp.models import CustomerUser
from catalog.models import ProductCategory, Product

from django import forms
from django.core.validators import ValidationError


class AdminUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''


class AdminProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''


class AdminProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''

