from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from openpyxl import Workbook
from datetime import datetime



# Função para exibir a lista de pessoas registradas
def lista_de_pessoas(request):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redireciona para a página de login se não estiver autenticado

    # Obtém todos os objetos do modelo Dados_cadastrais
    pessoas = Dados_cadastrais.objects.all()
    # Gera o URL para o menu inicial
    menu_inicial_url = reverse('menu')
    # Renderiza a página 'lista_pacientes.html' e passa os pacientes como contexto
    return render(request, 'app_de_cadastro/pessoas.html', {'pessoas': pessoas, 'menu_inicial_url': menu_inicial_url})

# Função para registrar um novo usuário
def registrar(request, template_name="registrar.html"):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redireciona para a página de login se não estiver autenticado

    form = DadosCadastraisForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('usuario_registrado')
        else:
            # Verificar se há campos em branco
            for field in form:
                if field.field.required and not field.data:
                    return HttpResponseBadRequest("Por favor, preencha todos os campos obrigatórios.")

    return render(request, 'app_de_cadastro/registrar.html', {'form': form})

# Função para exibir a página de registro concluído
def registrado(request, template_name="registrado.html"):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redireciona para a página de login se não estiver autenticado

    return render(request, 'app_de_cadastro/registrado.html')

# Função para deletar um usuário
def deletar_usuario(request):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redireciona para a página de login se não estiver autenticado

    if request.method == 'POST':
        usuario_ids = request.POST.get('usuario_ids')  # Obtém os IDs dos usuários a serem deletados
        if usuario_ids:
            ids_list = usuario_ids.split(',')
            Dados_cadastrais.objects.filter(id__in=ids_list).delete()  # Deleta os usuários selecionados
            return redirect('lista_de_pessoas')  # Redireciona para a página de lista de pessoas
    return redirect('lista_de_pessoas')  # Redireciona de volta para a lista de pessoas em caso de erro ou requisição GET

# Função para fazer login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Autenticação bem-sucedida
            user = form.get_user()
            login(request, user)
            return redirect('menu')  # Redireciona para o menu após o login
    else:   
        form = AuthenticationForm()
    return render(request, 'app_de_cadastro/login.html', {'form': form})

# Função para exibir o menu
def menu(request):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redireciona para a página de login se não estiver autenticado

    return render(request, 'app_de_cadastro/home.html')

# Função para fazer logout
def logout_view(request):
    logout(request)
    return redirect('user_login')

# Função para gerar um relatório em Excel
def gerar_relatorio_excel(request):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('user_login')  # Redireciona para a página de login se não estiver autenticado

    usuario_ids = request.GET.get('usuario_id')
    if not usuario_ids:
        return HttpResponseBadRequest("Usuário(s) não selecionado(s).")

    ids_list = usuario_ids.split(',')
    pessoas = Dados_cadastrais.objects.filter(id__in=ids_list)

    # Função auxiliar para remover o fuso horário de datetime
    def remove_timezone(dt):
        if dt is not None and dt.tzinfo is not None:
            return dt.replace(tzinfo=None)
        return dt

    # Cria um novo workbook e ativa a primeira worksheet
    wb = Workbook()
    ws = wb.active

    # Adiciona o cabeçalho na planilha
    ws.append(["Nome Completo", "Idade", "Responsável 1", "Responsável 2", "Telefone 1",
               "Telefone 2", "Principais Serviços", "Telefone 3", "Telefone 4",
               "Pessoa de Referência 1", "Pessoa de Referência 2", "Origem do Encaminhamento",
               "Demanda Inicial", "Início dos Atendimentos", "Data de Cadastro", "Profissional"])

    # Adiciona os dados de cada pessoa selecionada
    for pessoa in pessoas:
        ws.append([pessoa.nome, pessoa.idade, pessoa.responsavel_1, pessoa.responsavel_2,
                   pessoa.telefone_1, pessoa.telefone_2, pessoa.principais_servicos, pessoa.telefone_3,
                   pessoa.telefone_4, pessoa.pessoa_referencia_1, pessoa.pessoa_referencia_2,
                   pessoa.origem_do_encaminhamento, pessoa.demanda_inicial,
                   pessoa.inicio_dos_atendimentos, 
                   remove_timezone(pessoa.log_de_cadastro), 
                   pessoa.profissional])

    # Define o nome do arquivo
    file_name = f"relatorio_pessoas_selecionadas.xlsx"

    # Cria a resposta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={file_name}'

    # Salva o workbook na resposta HTTP
    wb.save(response)
    return response
