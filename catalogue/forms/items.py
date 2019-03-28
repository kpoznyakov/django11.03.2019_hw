from django import forms
from catalogue.models import Item


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
