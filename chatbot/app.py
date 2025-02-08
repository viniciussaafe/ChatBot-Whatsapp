from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Carregar as credenciais do Twilio das variáveis de ambiente
sid = os.getenv('TWILIO_ACCOUNT_SID')
authToken = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(sid, authToken)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    from_number = data.get('From')
    message_body = data.get('Body').lower().strip()
    
    response = MessagingResponse()
    if message_body == 'bom dia':
        response.message("Bom dia! Como posso ajudá-lo hoje?")
    else:
        response.message("Desculpe, não entendi sua mensagem.")
    
    return str(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
