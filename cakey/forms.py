from . models import Recipe
from django import forms

class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['user']
