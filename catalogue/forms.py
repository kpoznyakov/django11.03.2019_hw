from django import forms


class CreateCategoryForm(forms.Field):
    name = forms.CharField(max_length=255,
                           widget=forms.widgets.TextInput(
                               attrs={'class': 'form-field'}
                           )
                           )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea()
    )
