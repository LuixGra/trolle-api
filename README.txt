Trolle - Task Manager Fullstack (Quase-SaaS)

Aplicação fullstack de gerenciamento de tarefas (To-Do), com autenticação de usuários, API segura e interface moderna.
Projeto desenvolvido com foco em arquitetura profissional, escalabilidade e deploy real.


## Sobre o Projeto

O **Trolle** é um sistema web onde usuários podem:

* Criar conta e fazer login
* Criar, editar e deletar tarefas
* Marcar tarefas como concluídas
* Visualizar estatísticas no dashboard

Cada usuário possui suas próprias tarefas (multi-user com autenticação).


## Tecnologias Utilizadas

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT (Autenticação)
* Docker

### Frontend

* React
* Vite
* Axios
* CSS responsivo

### DevOps

* Docker & Docker Compose


## Arquitetura

Frontend → Backend → Banco de Dados

* React consome API REST do FastAPI
* Backend gerencia autenticação e regras de negócio
* PostgreSQL armazena usuários e tarefas

## Autenticação

* Login com JWT
* Proteção de rotas
* Senhas criptografadas com bcrypt

## Funcionalidades

* [x] Registro de usuário
* [x] Login com autenticação JWT
* [x] CRUD de tarefas
* [x] Marcar tarefa como concluída
* [x] Dashboard com estatísticas
* [x] Integração frontend + backend
* [x] Dockerização completa

## Rodando com Docker

docker-compose up --build
A aplicação estará disponível em:

* Frontend: http://localhost:5173
* Backend: http://localhost:8000
* Docs: http://localhost:8000/docs


## Deploy

* EM BREVE


## 🚀 Melhorias Futuras

* [ ] Refresh Token
* [ ] Sistema de filtros e busca
* [ ] Notificações (toast)
* [ ] Deploy com domínio próprio
* [ ] Sistema de planos (SaaS monetizado)(?)


## Autor

Desenvolvido por Luiz Graceli


## 📌 Observações

Este projeto foi desenvolvido com foco em aprendizado prático de:

* APIs modernas
* Autenticação segura
* Integração frontend/backend
* Containerização com Docker
* Deploy em produção


