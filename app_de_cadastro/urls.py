from django.urls import path
from . import views

urlpatterns = [
    
    # Rota para a página inicial
    path('', views.user_login, name='user_login'),
    # Rota para exibir o menu inicial
    path('menu/', views.menu, name='menu'),
    # Rota para exibir a lista de pessoas registradas
    path('pessoas/', views.lista_de_pessoas, name='lista_de_pessoas'),
    # Rota para exibir a lista de registros
    path('registrar/', views.registrar, name='registrar_usuario'),
    # Rota exibir mensagem de registro concluído
    path('registrado/', views.registrado, name='usuario_registrado'),
    # Rota para deletar usuário
    path('deletar/', views.deletar_usuario, name='deletar_usuario'),
    # Rota para deslogar
    path('logout/', views.logout_view, name='user_logout'),
    # Rota para Ferar relatório
    path('gerar_relatorio_excel/', views.gerar_relatorio_excel, name='gerar_relatorio_excel'),
]