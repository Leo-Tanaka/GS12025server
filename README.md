# EVACTECH - Servidor Simplificado

Servidor Flask para receber e armazenar o status de postes inteligentes.

## 🔄 Endpoints

### POST /status

Recebe status de um poste.

**JSON esperado:**
```json
{
  "poste_id": "P001",
  "status": "risco"
}
```

### GET /status

Retorna todos os dados armazenados.

**Filtragem por poste (opcional):**
```
/status?poste_id=P001
```

## ▶️ Como rodar

```bash
pip install -r requirements.txt
python app.py
```

## 🌐 Pronto para Render.com

- Crie um repositório no GitHub com esses arquivos
- Configure como Web Service no Render:
  - Build command: pip install -r requirements.txt
  - Start command: python app.py