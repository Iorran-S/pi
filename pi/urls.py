from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Configuração das URLs da aplicação
urlpatterns = [
    # URL para a administração do Django
    path('admin/', admin.site.urls),
    
    # Redireciona a raiz para a página de login do app_de_cadastro
    path('', RedirectView.as_view(url='app_de_cadastro/', permanent=False)),
    
    # URL para incluir as URLs da aplicação 'app_de_cadastro'
    # Certifique-se de adaptar o caminho ('app_de_cadastro.urls') conforme necessário
    path('app_de_cadastro/', include('app_de_cadastro.urls')),
]