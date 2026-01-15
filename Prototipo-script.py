import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- CONFIGURAÇÕES DA API (Você pega no painel da Z-API) ---
INSTANCIA_ID = "SUA_INSTANCIA_ID"
TOKEN_INSTANCIA = "SEU_TOKEN"
URL_API = f"https://api.z-api.io/instances/{INSTANCIA_ID}/token/{TOKEN_INSTANCIA}/send-text"

# --- LÓGICA DO MENU ---
config = {
    "1": "🥖 Pão Francês: R$ 12,90/kg",
    "2": "⏰ 06:00 às 20:00",
    "menu": "Olá! Digite 1 para Preços ou 2 para Horário."
}

def enviar_whatsapp(numero, texto):
    payload = {"phone": numero, "message": texto}
    # Envia a resposta de volta para a API do WhatsApp
    requests.post(URL_API, json=payload)

@app.route("/webhook", methods=['POST'])
def webhook():
    dados = request.get_json()
    
    # Pegando os dados vindos da Z-API
    # Nota: Verifique no painel da API os nomes exatos das chaves (Ex: 'text', 'phone')
    msg_cliente = dados.get('text', {}).get('message', '')
    telefone = dados.get('phone', '')

    if msg_cliente in config:
        resposta = config[msg_cliente]
    else:
        resposta = config["menu"]

    enviar_whatsapp(telefone, resposta)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=5000)