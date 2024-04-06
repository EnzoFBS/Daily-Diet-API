# Projeto: Daily Diet API

## Descrição
A **Daily Diet API** é uma aplicação desenvolvida em Flask para auxiliar no controle da dieta diária de usuários. Com esta API, os usuários podem registrar suas refeições, incluindo informações como nome, descrição, data e hora, e se a refeição está dentro da dieta ou não. Além disso, é possível editar, apagar, listar todas as refeições de um usuário e visualizar uma única refeição.

## Funcionalidades
- Registro de refeições, incluindo nome, descrição, data e hora, e status de inclusão na dieta.
- Edição de refeições, permitindo alterar todas as informações da refeição.
- Exclusão de refeições do banco de dados.
- Listagem de todas as refeições de um usuário.
- Visualização detalhada de uma única refeição.

## Tecnologias Utilizadas
- Flask: Framework web em Python utilizado para criar a API.
- Flask-SQLAlchemy: Extensão do Flask para interagir com bancos de dados SQL de forma simplificada.
- MySQL: Banco de dados relacional utilizado para armazenar as informações das refeições.
- Docker: Utilizado para containerizar o banco de dados MySQL, garantindo facilidade de configuração e portabilidade do ambiente de desenvolvimento.

## Como Executar o Projeto
1. Clone o repositório do projeto para sua máquina local.
2. Certifique-se de ter o Docker instalado.
3. Navegue até o diretório do projeto e execute o comando `docker-compose up -d` para iniciar o container do MySQL.
4. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.
5. Execute o arquivo `app.py` para iniciar a aplicação Flask.
6. Acesse a API através do navegador ou de ferramentas como Postman.

## Aprendizados
Este projeto proporcionou uma experiência prática valiosa no desenvolvimento de uma API utilizando o framework Flask, além de consolidar conhecimentos em integração com banco de dados SQL utilizando Flask-SQLAlchemy. Também aprendi sobre o uso do Docker para facilitar a configuração do ambiente de desenvolvimento e garantir a portabilidade do projeto.

## Conclusão
Desenvolver a **Daily Diet API** foi uma oportunidade de aplicar conceitos aprendidos durante o curso, além de adquirir novos conhecimentos e habilidades na construção de APIs RESTful em Python. Estou ansioso para explorar mais a fundo os recursos do Flask e continuar evoluindo minhas habilidades de desenvolvimento web.

## Autor
Seu nome ou apelido  
GitHub: EnzoFBS
LinkedIn: linkedin.com/in/enzo-silvestre/