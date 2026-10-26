# Cars

Sistema web de gerenciamento e catálogo de veículos desenvolvido com Django. O projeto permite cadastrar, listar, buscar, editar e excluir carros, com autenticação de usuários, upload de fotos, painel administrativo e geração automática de descrições com Inteligência Artificial.

## Demonstração

> Adicione aqui o link do deploy ou prints das telas do sistema.

## Funcionalidades

- Catálogo de carros com cards, foto, marca, modelo, ano e preço
- Busca de veículos por modelo
- Cadastro, edição e exclusão de carros (rotas protegidas por login)
- Detalhamento completo do veículo
- Cadastro de usuários, login e logout
- Upload e exibição de imagens dos veículos
- Geração automática de descrição do carro com IA (OpenAI)
- Inventário automático com quantidade e valor total dos carros, atualizado por signals
- Painel administrativo do Django para gerenciar marcas e carros
- Interface responsiva em HTML/CSS puro

## Tecnologias

| Camada | Tecnologias |
| --- | --- |
| Backend | Python 3.13, Django 6 |
| Banco de dados | PostgreSQL 16 |
| IA | OpenAI API (Responses API) |
| Configuração | pydantic-settings, variáveis de ambiente |
| Infraestrutura | Docker Compose |
| Qualidade de código | Ruff, Taskipy, uv |

## Arquitetura

O projeto está organizado em apps Django com responsabilidades bem definidas:

```
.
├── app/            # Configurações do projeto, URLs e templates base
├── accounts/       # Autenticação: registro, login e logout
├── cars/           # Modelos, views, forms, signals e templates de carros
├── openai_api/     # Cliente e integração com a OpenAI
├── config.py       # Carregamento tipado das variáveis de ambiente
├── docker-compose.yaml
├── manage.py
└── pyproject.toml
```

### Modelos principais

- **Brand**: marca do veículo.
- **Car**: modelo, marca, ano de fabricação, ano do modelo, placa, valor, foto e descrição (`bio`).
- **CarInventory**: histórico com quantidade e valor total do estoque, gerado automaticamente.

### Destaques de implementação

- **Signals**: ao salvar um carro sem descrição, a `bio` é gerada via IA (`pre_save`). A cada criação ou exclusão, o inventário é recalculado (`post_save` / `post_delete`).
- **Formulários com validação**: regras de negócio como valor mínimo de R$ 20.000 e ano de fabricação a partir de 1975.
- **Class-based views**: uso de `ListView`, `DetailView`, `CreateView`, `UpdateView` e `DeleteView`.
- **Configuração tipada**: `pydantic-settings` valida as variáveis de ambiente na inicialização.

## Rotas

| Rota | Descrição |
| --- | --- |
| `/cars/` | Listagem e busca de carros |
| `/new_car/` | Cadastro de carro (requer login) |
| `/car/<id>/` | Detalhes do carro |
| `/car/<id>/update/` | Edição do carro (requer login) |
| `/car/<id>/delete/` | Exclusão do carro (requer login) |
| `/register` | Cadastro de usuário |
| `/login/` | Login |
| `/logout` | Logout |
| `/admin/` | Painel administrativo |

## Como executar

### Pré-requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- Docker e Docker Compose
- Chave de API da OpenAI

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/williangaia/cars.git
cd cars

# 2. Configure as variáveis de ambiente
cp .env.example .env
# edite o .env com suas credenciais

# 3. Suba o banco de dados
docker compose up -d

# 4. Instale as dependências
uv sync

# 5. Rode as migrações
uv run manage.py migrate

# 6. Crie um superusuário (para acessar o admin)
uv run manage.py createsuperuser

# 7. Inicie o servidor
uv run manage.py runserver
```

A aplicação estará disponível em `http://localhost:8000`.

## Variáveis de ambiente

Crie o arquivo `.env` a partir do `.env.example`:

```env
OPENAI_API_KEY=api_key

POSTGRES_DB=db_name
POSTGRES_USER=db_username
POSTGRES_PASSWORD=db_username_password
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

## Scripts úteis

Os comandos estão disponíveis via Taskipy:

```bash
task run              # Inicia o servidor de desenvolvimento
task migrate          # Aplica as migrações
task makemigrations   # Cria novas migrações
task shell            # Abre o shell do Django
task check            # Verifica o projeto
task lint             # Executa o Ruff
task format           # Formata o código
```

## Aprendizados

Este projeto foi desenvolvido para praticar e demonstrar:

- Estruturação de projetos Django em apps reutilizáveis
- Autenticação e autorização de usuários
- CRUD completo com class-based views
- Uso de signals para automação de regras de negócio
- Integração com APIs de IA e tratamento de erros
- Containerização do banco de dados com Docker
- Configuração segura por variáveis de ambiente
- Padronização e qualidade de código com Ruff

## Autor

**[Willian Gaia Pereira](https://github.com/williangaia)**

Projeto desenvolvido como parte do portfólio de desenvolvimento backend com Python e Django
