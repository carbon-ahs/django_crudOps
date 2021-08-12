from django import forms
from .models import Product
'''
from .models import ModelName
class ModelNameForm(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = '__all__'
'''

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'