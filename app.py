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
        raw = request.data.decode('utf-8')
        print(f"[BRUTO] JSON recebido: {raw}")

        data = request.get_json(force=True, silent=True)

        if data is None:
            print("[ERRO] Falha ao interpretar JSON")
            return jsonify({"error": "JSON inválido ou ausente"}), 400

        if not all(field in data for field in ("poste_id", "status")):
            print("[ERRO] JSON incompleto:", data)
            return jsonify({"error": "Campos obrigatórios ausentes"}), 400

        data["timestamp"] = datetime.now().isoformat()
        status_data.append(data)

        print(f"[RECEBIDO] Poste: {data['poste_id']} | Status: {data['status']} | Hora: {data['timestamp']}")

        return jsonify({"message": "Status recebido com sucesso."}), 200

    except Exception as e:
        print(f"[EXCEÇÃO] {e}")
        return jsonify({"error": "Erro interno"}), 500

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