# Biblioteca Virtual - Django

Este é um sistema de gestão de uma biblioteca virtual, desenvolvido em Django como parte de um desafio técnico. O sistema permite o gerenciamento completo de empréstimos de livros, voltado para bibliotecas ou sistemas de empréstimos internos de empresas ou instituições.

---

## Funcionalidades

### Leitores
- **Visualizar Livros Disponíveis**: Acesso à lista de livros que estão disponíveis para empréstimo.
- **Solicitar Empréstimos**: Possibilidade de solicitar o empréstimo de um livro.
- **Histórico de Empréstimos**: Consulta ao histórico de empréstimos realizados.

### Administradores
- **Gerenciamento do Acervo**: Cadastrar novos livros e inativar livros existentes.
- **Aprovar e Concluir Empréstimos**: Aprovar solicitações de empréstimo e registrar a devolução (conclusão) de empréstimos.
- **Relatório de Empréstimos**: Consultar relatórios de empréstimos filtrados por período.

---

## Estrutura do Projeto

O projeto segue a estrutura padrão de um projeto Django, com aplicativos para usuários, livros e empréstimos:

- **biblioteca**: Contém as configurações do projeto.
- **usuarios**: Gerenciamento de usuários, incluindo o redirecionamento para as páginas de acordo com o tipo de usuário (leitor ou administrador).
- **livros**: Gerenciamento de livros, incluindo cadastro e inativação.
- **emprestimos**: Gerenciamento de empréstimos, com funcionalidades de solicitação, aprovação, conclusão e geração de relatórios.

---

## Instalação e Configuração

### Pré-requisitos

- Python 3.x
- Django (versão usada no projeto)
- Repositório Git (para clonar o projeto)

### Passo a Passo

1. **Clone o Repositório:**

    ```bash
    git clone https://github.com/FernandoFigdev/Biblioteca_Virtual-Django.git
    cd Biblioteca_Virtual-Django
    ```

2. **Crie um Ambiente Virtual:**

    - Para Linux/macOS:
    
      ```bash
      python -m venv env
      source env/bin/activate
      ```

    - Para Windows:
    
      ```bash
      python -m venv env
      env\Scripts\activate
      ```

3. **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurações do Django:**

    - Execute as migrações para criar o banco de dados:

      ```bash
      python manage.py migrate
      ```

    - Crie um superusuário para acessar o Django Admin:

      ```bash
      python manage.py createsuperuser
      ```

    - Inicie o Servidor:

      ```bash
      python manage.py runserver
      ```

    Acesse o sistema em [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

---

## Uso

### Login

- Acesse a tela de login e entre com suas credenciais.
- Os administradores são redirecionados para o painel administrativo, enquanto os leitores são redirecionados para a tela de solicitações de empréstimo.

### Funcionalidades dos Administradores

- **Cadastrar Livros**: Clique em "Cadastrar Novo Livro" no painel de administrador para ser direcionado à página de cadastro.
- **Aprovar Empréstimos**: Acesse a seção de empréstimos pendentes e clique no botão "Aprovar" para confirmar.
- **Concluir Empréstimos**: Registre a devolução de livros na seção de empréstimos aprovados.
- **Consultar Relatórios**: Insira uma data inicial e uma final para gerar um relatório de empréstimos no período especificado.

### Funcionalidades dos Leitores

- **Visualizar Livros Disponíveis**: Veja a lista de livros disponíveis para empréstimo.
- **Solicitar Empréstimo**: Escolha um livro e faça a solicitação, que será aprovada posteriormente por um administrador.
- **Histórico de Empréstimos**: Veja as solicitações e os empréstimos concluídos.

---

## Tecnologias Utilizadas

- **Django**: Framework principal para o backend.
- **Django REST Framework**: Implementação de APIs.
- **HTML/CSS**: Estrutura e estilo das páginas.
- **JavaScript**: Funcionalidades de front-end.

---

## Estrutura do Código

- **urls.py**: Configura as rotas do projeto, organizadas por função e aplicativo.
- **views.py**: Lógica para cada endpoint, incluindo a validação de permissões e status de empréstimos.
- **models.py**: Definição das tabelas para Usuário, Livro e Empréstimo.
- **serializers.py**: Serializadores para a comunicação via API REST.

---

## Próximos Passos

- Adicionar melhorias na interface com mais feedback visual para o usuário.
- Considerar a expansão de relatórios para incluir dados adicionais, como histórico completo do acervo.
