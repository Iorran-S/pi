from django import forms
from .models import Dados_cadastrais

class DadosCadastraisForm(forms.ModelForm):
    class Meta:
        model = Dados_cadastrais
        fields = '__all__'  # Ou especifique os campos se preferir

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nome Completo",
                                    required= True)
    
    idade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label="Idade")

    responsavel_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                     label="Responsável 1")
    
    responsavel_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                     label="Responsável 2", required=False)
    
    telefone_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label="Telefone 1")
    
    telefone_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label="Telefone 2", required=False)
    
    principais_servicos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                          label="Principais Serviços")
    
    telefone_3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label="Telefone 3", required=False)
    
    telefone_4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label="Telefone 4", required=False)
    
    pessoa_referencia_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                           label="Pessoa de Referência 1", required=False)
    
    pessoa_referencia_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                           label="Pessoa de Referência 2", required=False)
    
    origem_do_encaminhamento = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                                                label="Origem do Encaminhamento", required=False)
    
    demanda_inicial = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                                       label="Demanda Inicial", required=False)
    
    inicio_dos_atendimentos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                               label="Início dos Atendimentos", required=False)
    
    profissional = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   label="Profissional")

from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)