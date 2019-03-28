from django import forms
from catalogue.models import Category


# медленный и накладный способ. Использовать только в случае создания нестандартных форм с нестандартным поведением
class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=255,
                           widget=forms.widgets.TextInput(
                               attrs={'class': 'form-field'}
                           )
                           )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-field'}
        )
    )


# быстрый способ
class CreateCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc']
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={'class': 'form-field'}),
            'desc': forms.widgets.Textarea(
                attrs={'class': 'form-field'})
        }
