from django import forms

from ..models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario

        fields = ['nome', 'cpf','imagem', 'telefone', 'rua', 'cidade', 'bairro','numero_casa', 'email', 'password']


class FuncionarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario

        fields = ['nome', 'cpf','imagem', 'telefone', 'rua', 'cidade', 'bairro','numero_casa', 'email', 'password', 'nivel']
