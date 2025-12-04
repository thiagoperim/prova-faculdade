import re

from django import forms

from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'documento', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite aqui', 'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite aqui', 'class': 'input-field'}),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Digite aqui',
                    'class': 'input-field',
                    'autocomplete': 'tel',
                    'inputmode': 'numeric',
                    'pattern': '[0-9]*',
                    'oninput': "this.value=this.value.replace(/\\D/g,'')",
                }
            ),
            'documento': forms.ClearableFileInput(attrs={'class': 'file-input'}),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder': 'Digite aqui',
                    'class': 'textarea-field',
                    'rows': 4,
                }
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome) < 2:
            raise forms.ValidationError('Nome muito curto, coloque pelo menos 2 letras.')
        return nome

    def clean_telefone(self):
        telefone = (self.cleaned_data.get('telefone') or '').strip()
        digits = re.sub(r'\D', '', telefone)
        if len(digits) < 8:
            raise forms.ValidationError('Telefone muito curto, verifique.')
        if len(digits) > 11:
            raise forms.ValidationError('Limite de 11 caracteres, por favor, verifique seu número.')
        return digits

    def clean_mensagem(self):
        mensagem = (self.cleaned_data.get('mensagem') or '').strip()
        if len(mensagem) < 5:
            raise forms.ValidationError('Mensagem muito curta, explique melhor.')
        return mensagem
