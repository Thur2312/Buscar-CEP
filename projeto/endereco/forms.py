from django import forms
from .models import Address

class CePForm(forms.Form):
    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            'cep': 'CEP',
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'localidade': 'Localidade',
            'uf': 'UF'
        }
        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
        }   
class AddressForm(forms.ModelForm):
    class Meta: 
        model = Address
        fields = '__all__'
        labels = {
            'cep': 'CEP',
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'localidade': 'Localidade',
            'uf': 'UF'
        }
        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
        }   