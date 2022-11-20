from django import forms

from imoveis.models import Imovel

class ImovelForm(forms.ModelForm):
    area = forms.CharField(label='Area', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'Informe a Area'}))

    rua = forms.CharField(label='Rua', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'Informe a Rua'}))

    bairro = forms.CharField(label='Bairro', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'Informe a Bairro'}))

    cidade = forms.CharField(label='Cidade', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'Informe a Cidade'}))

    numero = forms.IntegerField(label='numero', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':  'Informe o Numero'}))

    valor = forms.FloatField(label='valor', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':  'Informe o valor'}))

    """imagem = forms.ImageField(label='imagem', widget=forms.TextInput(attrs={'type': 'file', 'placeholder':  'Informe o imagem'}))"""

    categoria = forms.CharField(label='categoria', widget=forms.Select(attrs={'class': 'form-control'}, choices= [
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Terreno', 'Terreno'),
        ('Predio comercial', 'Predio comercial'),
    ]))
    class Meta:
        model = Imovel

        fields = '__all__'
