# Projeto de Cadastro em Django

Este é um projeto de cadastro simples desenvolvido em Django. Ele permite que os usuários registrem informações em um banco de dados e visualizem esses registros.

## Estrutura do Projeto

pi/

├── app_de_cadastro/

├── pi/

├── templates/

├── manage.py

├── requirements.txt

├── .env

└── README.md


## Pré-requisitos

- Python 3.x
- Pip (Python package installer)
- Virtualenv (recomendado)

## Configuração do Ambiente de Desenvolvimento

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/Iorran-S/App_de_cadastro.git
   cd pi

2. **Crie um ambiente virtual:**

   ```sh
   python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate

3. **Instale as dependências:**

   ```sh
pip install -r requirements.txt

4. **Configure as variáveis de ambiente:**

Crie um arquivo .env na raiz do projeto com as seguintes configurações:

DEBUG=True
SECRET_KEY=sua_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]


5. **Realize as migrações do banco de dados:**

   ```sh
python manage.py migrate

6. **Execute o servidor de desenvolvimento:**

   ```sh
Acesse a aplicação em http://127.0.0.1:8000/app_de_cadastro/.

# Implantação no Render

## Configure o repositório:

Certifique-se de que o seu repositório está configurado no GitHub, GitLab, ou outro serviço.

### Conecte ao Render:

Vá para Render e faça login.
Crie um novo serviço Web e conecte ao seu repositório.

### Configurações do Render:

Build Command: pip install -r requirements.txt
Start Command: gunicorn projeto.wsgi:application

## Variáveis de Ambiente no Render:
### Adicione as variáveis de ambiente no painel do Render, por exemplo:

DEBUG=False
SECRET_KEY=sua_secret_key_de_producao
ALLOWED_HOSTS=example.onrender.com

### Deploy:

Render irá automaticamente detectar novos commits e reimplantar a aplicação. Verifique os logs no painel do Render para garantir que o deploy foi bem-sucedido.

Estrutura de Arquivos
app_de_cadastro/: Contém os modelos, views, e templates do aplicativo de cadastro.
projeto/: Configurações principais do projeto Django.
templates/: Arquivos HTML para renderização das páginas.
manage.py: Script de gerenciamento do Django.
requirements.txt: Lista de dependências do projeto.
.env: Variáveis de ambiente (não incluído no repositório por segurança).

# Contribuição

Clone este repositório.
Crie uma branch (git checkout -b feature/MinhaFeature).
Commit suas alterações (git commit -am 'Adiciona nova feature').
Push para a branch (git push origin feature/MinhaFeature).
Crie um novo Pull Request.

# Licença

Este projeto está licenciado sob os termos da MIT License.


### Explicação

- **Título e Descrição**: Uma breve descrição do projeto.
- **Estrutura do Projeto**: Uma visão geral da estrutura do diretório do projeto.
- **Pré-requisitos**: Lista de softwares necessários para executar o projeto.
- **Configuração do Ambiente de Desenvolvimento**: Instruções passo a passo para configurar o ambiente local.
- **Implantação no Render**: Guia para implantar o projeto no Render.
- **Estrutura de Arquivos**: Descrição dos diretórios e arquivos principais.
- **Contribuição**: Instruções para contribuidores.
- **Licença**: Informação sobre a licença do projeto.
