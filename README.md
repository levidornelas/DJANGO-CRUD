# DJANGO-CRUD
# Django CRUD Project with MySQL

Este projeto é um sistema simples de CRUD (Create, Read, Update, Delete) desenvolvido em Python utilizando o framework Django e o banco de dados MySQL. O sistema permite a criação, leitura, atualização e exclusão de produtos, além de incluir uma funcionalidade de envio de e-mail simulado.

## Funcionalidades

- **Listagem de Produtos**: Exibe todos os produtos cadastrados.
- **Busca de Produtos**: Permite a busca de produtos por nome.
- **Cadastro de Produtos**: Interface para cadastrar novos produtos.
- **Atualização de Produtos**: Interface para atualizar informações de produtos existentes.
- **Exclusão de Produtos**: Interface para deletar produtos.
- **Envio de E-mail Simulado**: Funcionalidade de envio de e-mail implementada localmente sem servidor SMTP.
- **Check de login**: Caso você não esteja logado por meio da rota /admin, as implementações para criar, atualizar e deletar produto não funcionam.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Framework**: Django 4.x
- **Banco de Dados**: MySQL
- **Outros**: Bootstrap para estilização

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/levidornelas/DJANGO-CRUD

2. **Crie um ambiente virtual**:
```
  python3 -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate  # Windows
```

3. **Instale as dependências**:
  ```
  pip install -r requirements.txt
  ```

4. **Configure o banco de dados MySQL**:

- Crie um banco de dados no MySQL.
- Atualize as configurações de conexão com o banco de dados no arquivo settings.py.


5. **Realize as migrações do banco de dados:**
```
python manage.py migrate
```

5. **Crie o "superuser" que lhe permitirá fazer o CRUD:**
```
python manage.py createsuperuser
```

6. **Rode o servidor localmente**:
```
python manage.py runserver
```

## Uso

- Acesse `http://localhost:8000` para visualizar a página inicial.
- Navegue pelas funcionalidades de listagem, busca, criação, atualização e exclusão de produtos.
- A funcionalidade de envio de e-mail pode ser testada na página de contato.

## Contribuição
Sinta-se livre para criar pull requests e contribuir com o projeto.

## Licença
Este projeto é licenciado sob a Licença MIT.