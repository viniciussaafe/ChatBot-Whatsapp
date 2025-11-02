<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRO5PLNl-HQOO7ukJbratFMj071iulSNd9lg&s" alt="ChatBot">
</p>

💬 Twilio SMS Webhook com Flask

Este é um projeto simples em Python utilizando o framework Flask para criar um webhook que responde a mensagens SMS recebidas via Twilio.

O objetivo é demonstrar a configuração básica de um endpoint (/webhook) para processar mensagens e retornar uma resposta em formato TwiML (XML).

🚀 Tecnologias Utilizadas

    Python: Linguagem de programação principal.

    Flask: Micro-framework web para criar o servidor.

    Twilio Python Helper Library: Para gerar a resposta TwiML (MessagingResponse) e interagir com a API.

    python-dotenv: Para gerenciar as variáveis de ambiente (credenciais da Twilio).

🛠️ Pré-requisitos

Para rodar este projeto, você precisará de:

    Python 3.x instalado.

    Uma conta Twilio (com um número de telefone configurado).

    pip (gerenciador de pacotes do Python).

    Um serviço para expor seu servidor local à internet (como Ngrok), pois o Twilio precisa de um URL público para enviar o webhook.

Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e as credenciais.

1. Clonar o Repositório e Instalar Dependências

Crie a estrutura do seu projeto e instale as bibliotecas necessárias.
Bash

# Instala as bibliotecas listadas no seu ambiente
pip install Flask twilio python-dotenv

2. Configurar Variáveis de Ambiente

Crie um arquivo chamado .env na raiz do projeto para armazenar suas credenciais de forma segura. Substitua os placeholders pelos seus dados reais da conta Twilio.

.env

TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
TWILIO_AUTH_TOKEN=your_auth_token_here

3. Estrutura do app.py

O arquivo principal app.py deve conter o código para iniciar o Flask e definir o endpoint do webhook, utilizando as variáveis de ambiente carregadas.

    (O conteúdo do seu app.py deve ser inserido aqui, com a lógica de resposta definida.)

💡 Lógica do Webhook

O endpoint /webhook é o coração do projeto. Ele recebe uma requisição POST da Twilio sempre que uma mensagem SMS é enviada para o seu número.

    Recebimento: O código extrai a mensagem ('Body') da requisição e a formata para minúsculas.

    Processamento:

        Se a mensagem for exatamente 'bom dia' (ignorando maiúsculas e minúsculas), ele retorna uma saudação amigável.

        Caso contrário, ele retorna uma mensagem padrão informando que não entendeu.

    Resposta: A resposta é convertida em uma string TwiML (XML) e enviada de volta para a Twilio.

🏃 Como Executar

1. Iniciar o Servidor Flask

Execute o script Python. Por padrão, ele rodará na porta 5000.
Bash

python app.py

O console mostrará que o servidor está rodando:

    Running on http://127.0.0.1:5000/

2. Expor o Servidor (Ngrok)

Para que a Twilio possa acessar o seu servidor local, você precisa expor a porta 5000 usando Ngrok (ou uma ferramenta similar):
Bash

ngrok http 5000

O Ngrok fornecerá um URL público, por exemplo: https://abcd1234.ngrok-free.app

3. Configuração na Twilio

    Acesse o Console da Twilio.

    Navegue até o número de telefone Twilio que você está usando.

    Na seção "Messaging", encontre a opção "A Message Comes In".

    Configure o método como HTTP POST e o URL como:

    https://abcd1234.ngrok-free.app/webhook

    (Substitua o endereço pelo seu URL gerado pelo Ngrok.)

✅ Teste

Envie um SMS para o seu número Twilio com as seguintes mensagens e observe a resposta:
Mensagem Enviada	Resposta Esperada
bom dia	Bom dia! Como posso ajudá-lo hoje?
BOM DIA	Bom dia! Como posso ajudá-lo hoje?
oi	Desculpe, não entendi sua mensagem.
