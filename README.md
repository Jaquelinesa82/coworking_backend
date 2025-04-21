# 🌐 Coworking Metaverso Backend

Este projeto é o backend de um MVP de ambiente virtual.

---

## 🧠 Objetivo

Oferecer um ambiente de coworking virtual, onde qualquer pessoa ou empresa possa criar salas para interações com recursos digitais, como:
- Chat, quadro branco, vídeos e outras ferramentas
- Perfis personalizados com avatar
- Controle de participantes com papéis (host, moderador, speaker, viewer)

---


## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- UUID + JSONField para flexibilidade e identificação
- Pytest + Factory Boy para testes

---

## 🧪 Execução Local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/coworking_backend.git
cd coworking_backend

# Ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalação de dependências
pip install -r requirements.txt

# Migrations
python manage.py migrate

# Executar servidor
python manage.py runserver

```

## 👩‍💻 Autoria
Em desenvolvimento por Jaqueline Santos
