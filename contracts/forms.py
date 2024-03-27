from django import forms
from .models import Contracts

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = 'name', 'product', 'cost', 'start_data', 'end_data', 'file'
        widgets = {
            'start_data': forms.SelectDateWidget(),
            'end_data': forms.SelectDateWidget(),
        }