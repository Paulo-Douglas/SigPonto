# 🕒 SigPonto

Sistema de controle de ponto digital para servidores da UFRN – Campus Ceres.

## 📦 Tecnologias Utilizadas

**Backend:** Django + FastAPI + Docker

**Frontend:** Flutter (desenvolvido e testado para Linux)

## ⚙️ Como executar o projeto

### Backend

```bash
cd src/backend
docker compose down      # Encerra containers existentes (caso estejam ativos)
docker compose build     # Constrói a imagem do backend
docker compose up        # Inicia o backend na porta localhost:8000
```

### Frontend

```bash
cd src/frontend
flutter pub get          # Pegar as depedências do projeto no pubspec.yaml
flutter run              # Executa o app (desenvolvido para dispositivo Linux)
```

## 🔐 API – Endpoints

### POST /api/login

- **Descrição:** Autentica um servidor.
- **Requisição:** JSON com `username`
- **Resposta:** Token de autenticação

### POST /api/logout

- **Descrição:** Encerra a sessão do servidor.
- **Requisição:** JSON com `username`
- **Resposta:** HTTP 204 (No Content) em caso de sucesso

### GET /api/ponto

- **Descrição:** Lista os registros de ponto de um servidor.
- **Requisição:** Query param `username`
- **Resposta:** Lista de registros de ponto

### POST /api/ponto

- **Descrição:** Registra um novo ponto para o servidor autenticado.
- **Requisição:**
  - Header: `Authorization: Bearer <token>`
  - Body JSON: `{ "latitude": <float>, "longitude": <float> }`
- **Resposta:** Dados do ponto registrado

## 📌 Observações

É necessário que o backend esteja rodando antes de iniciar o frontend.

O projeto foi testado com o Flutter em ambiente Linux; outras plataformas podem exigir ajustes.
