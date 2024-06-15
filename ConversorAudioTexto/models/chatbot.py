from twilio.rest import Client

# Credenciais do ChatBot para uso no WhatsApp
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Função para enviar mensagem de bom dia
def enviar_mensagem_bom_dia(numero_destino):
    mensagem = "Bom dia! Tenha um ótimo dia!"
    from_whatsapp_number = 'whatsapp:+14155238886'  # Seu número do WhatsApp no Twilio
    to_whatsapp_number = f'whatsapp:{numero_destino}'

    message = client.messages.create(
        body=mensagem,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(f"Mensagem enviada: {message.sid}")

# Exemplo de uso
if __name__ == "__main__":
    numero_destino = '+5511999999999'  # Número de telefone do destinatário
    enviar_mensagem_bom_dia(numero_destino)
