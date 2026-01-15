from flask import Flask, request, jsonify

app = Flask(__name__)

# --- MESMA CONFIGURAÇÃO DO BOT ANTERIOR ---
config = {
    "menu_principal": (
        "Olá! Bem-vindo à Padaria. 🥖\n"
        "1. Preços\n2. Horário\n3. Localização"
    ),
    "opcoes": {
        "1": "🥖 Pão Francês: R$ 12,90/kg",
        "2": "⏰ 06:00 às 20:00",
        "3": "📍 Rua das Flores, 123"
    }
}

# --- A ROTA QUE RECEBE A MENSAGEM DO WHATSAPP ---
@app.route("/webhook", methods=['POST'])
def webhook():
    # 1. Recebe os dados enviados pela API do WhatsApp
    dados = request.get_json()
    
    # 2. Extrai o texto e o número de quem enviou (o formato varia por API)
    # Aqui usamos nomes genéricos ['message'] e ['sender']
    try:
        msg_cliente = dados.get('message', '').strip()
        telefone_cliente = dados.get('sender', '')

        # 3. Lógica do Menu (Mesma do VS Code)
        if msg_cliente in config["opcoes"]:
            resposta = config["opcoes"][msg_cliente]
        else:
            resposta = config["menu_principal"]

        # 4. LOG no terminal para você acompanhar
        print(f"Mensagem de {telefone_cliente}: {msg_cliente}")
        print(f"Resposta enviada: {resposta}")

        # 5. Retorna a resposta para a API enviar ao cliente
        return jsonify({"status": "sucesso", "resposta": resposta}), 200

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"status": "erro"}), 500

if __name__ == "__main__":
    # Roda o servidor na porta 5000
    app.run(host='0.0.0.0', port=5000)