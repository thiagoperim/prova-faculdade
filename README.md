# Prova AV2 - Fale Conosco (Django)

Projeto simples em Django/DRF para a prova da faculdade. Inclui formulário de contato com upload de PDF, listagem via API e administração pelo Django Admin.

## Requisitos
- Python 3.12+
- SQLite (já vem por padrão)
- Dependências: ver `requirements.txt`

## Como rodar
1. Instalar dependências:
   ```bash
   py -m pip install -r requirements.txt
   ```
2. Aplicar migrations:
   ```bash
   py manage.py migrate
   ```
3. Criar superusuário para acessar o admin:
   ```bash
   py manage.py createsuperuser
   ```
4. Subir o servidor:
   ```bash
   py manage.py runserver
   ```

## Uso
- Formulário: acessar seu localhost e enviar Nome, Email, Telefone (8 a 11 dígitos), Mensagem e PDF.
- Admin: `/admin/` (usar o superuser criado).
- API (somente GET): `/api/contatos/` retorna JSON com os contatos e URLs dos PDFs.

## Estrutura MVT resumida
- Model: `faleconosco/models.py` (Contato, validações de PDF e tamanho da mensagem)
- View: `faleconosco/views.py` (`contato_view` salva e mostra mensagens; `ContatoListAPIView` expõe a lista em JSON)
- Template: `faleconosco/templates/faleconosco/contato.html` (layout e form)
- Form: `faleconosco/forms.py` (campos, widgets e validações simples)
- URLs: `prova_av2/urls.py` (inclui app) e `faleconosco/urls.py` (rota do form e API)
- Estilos: `faleconosco/static/faleconosco/styles.css`

## Observações
- Uploads vão para `media/documentos/`; arquivos estáticos servidos de `static/` em debug.
