from django import forms
from .models import Allergies

class AllergiesForm(forms.ModelForm):
    class Meta:
        model = Allergies
        fields = ['name',
        'bool_0',
        'bool_1',
        'bool_2',
        'bool_3',
        'bool_4',
        'bool_5',
        'bool_6',
        'bool_7',
        'bool_8',
        'bool_9',
        'bool_10',
        'bool_11']