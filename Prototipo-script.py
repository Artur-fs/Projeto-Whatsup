import time

# 1. Configuração do "Cérebro" do Bot (Fácil de alterar para qualquer comércio)

config = {
    "nome_loja": "Padaria do Bairro",
    "menu_principal": (
        "Olá! Bem-vindo à Padaria do Bairro. 🥖\n"
        "Digite o número da opção desejada:\n"
        "1. Ver preços do dia\n"
        "2. Horário de funcionamento\n"
        "3. Localização\n"
        "4. Falar com um humano"
    ),
    "opcoes": {
        "1": "🥖 Pão Francês: R$ 12,90/kg\n🥐 Croissant: R$ 5,00/un\n☕ Café: R$ 4,00",
        "2": "⏰ Aberto todos os dias, das 06:00 às 20:00.",
        "3": "📍 Rua das Flores, nº 123 (Ao lado do mercado).",
        "4": "Entendido! Vou chamar o João. Aguarde um instante... 🙋‍♂️"
    }
}

def processar_mensagem(texto):
    
    """Simula a recepção de uma mensagem e retorna a resposta"""
    
    texto = texto.strip()
    
    # Se o cliente digitar um número que está no nosso menu
    
    if texto in config["opcoes"]:
        return config["opcoes"][texto]
    
    # Se for uma saudação ou qualquer outra coisa, mostra o menu principal
    
    else:
        return config["menu_principal"]

# --- SIMULAÇÃO DE FUNCIONAMENTO ---

print("--- SISTEMA DE AUTOMAÇÃO INICIADO ---")
print("Aguardando mensagens... (Pressione Ctrl+C para parar)\n")

while True:
    msg_cliente = input("Cliente diz: ") # Simula a mensagem chegando do WhatsApp
    
    print("Bot respondendo...")
    time.sleep(0.5) # Simula um pequeno delay humano
    
    resposta = processar_mensagem(msg_cliente)
    print(f"\n[WHATSAPP]: {resposta}\n")
    print("-" * 30)