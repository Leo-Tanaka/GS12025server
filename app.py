from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Armazena os dados recebidos
status_data = []

@app.route('/')
def index():
    return "Servidor EVACTECH ativo."

@app.route('/status', methods=['POST'])
def receber_status():
    try:
        data = request.get_json()

        # Verifica campos obrigatórios
        if not all(field in data for field in ("poste_id", "status")):
            print("[ERRO] JSON incompleto:", data)
            return jsonify({"error": "Campos 'poste_id' e 'status' são obrigatórios."}), 400

        # Timestamp e armazenamento
        data["timestamp"] = datetime.now().isoformat()
        status_data.append(data)

        # Log completo
        print(f"[RECEBIDO] Poste: {data['poste_id']} | Status: {data['status']} | Hora: {data['timestamp']}")

        return jsonify({"message": "Status recebido com sucesso."}), 200

    except Exception as e:
        print(f"[EXCEÇÃO] {e}")
        return jsonify({"error": "Erro ao processar os dados."}), 500

@app.route('/status', methods=['GET'])
def listar_status():
    poste_id = request.args.get("poste_id")

    if poste_id:
        filtrado = [d for d in status_data if d["poste_id"] == poste_id]
        return jsonify(filtrado), 200

    return jsonify(status_data), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)