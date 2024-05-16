from django.db import models


# Modelo representando as pessoas atendidas
class Dados_cadastrais(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo", blank=True)
    idade = models.IntegerField(verbose_name="Idade", blank=True)
    responsavel_1 = models.CharField(max_length=150)
    responsavel_2 = models.CharField(max_length=150, blank=True) # Permite campos em branco
    telefone_1 = models.CharField(max_length=20)
    telefone_2 = models.CharField(max_length=20, blank=True) # Permite campos em branco
    principais_servicos = models.CharField(max_length=300)
    telefone_3 = models.CharField(max_length=20, blank=True) # Permite campos em branco
    telefone_4 = models.CharField(max_length=20, blank=True) # Permite campos em branco
    pessoa_referencia_1 = models.CharField(max_length=150, blank=True) # Permite campos em branco
    pessoa_referencia_2 = models.CharField(max_length=150, blank=True) # Permite campos em branco
    origem_do_encaminhamento = models.TextField(blank=True) # Permite campos em branco
    demanda_inicial = models.TextField(blank=True)  # Permite campos em branco
    inicio_dos_atendimentos = models.TextField(blank=True)  # Permite campos em branco
    log_de_cadastro = models.DateTimeField(auto_now_add=True)  # Registra a data e hora automaticamente ao criar o registro
    profissional = models.CharField(max_length=150)

    def __str__(self):
        return f"Registro completo de {self.nome} em: {self.log_de_cadastro}!"