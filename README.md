# 🍼 BabyStore Checkout – Python + Flask + Asaas

Aplicação web desenvolvida com Python Flask que permite adicionar produtos a um carrinho de compras simples, calcular subtotal, escolher quantidade de parcelas e gerar automaticamente um link de pagamento do Asaas, redirecionando o usuário diretamente para a página de pagamento com Cartao de Credito.


O projeto foi divido em 3 partes

1 - Criacao da conta no Asaas. Cria-se primeiro porque caso precise usar as funcoes em producoes no mundo real (como trabalhar dinheiro real) demora a validacao da empresa pois precisa enviar documentacao.

2 - Criacao do codigo base que vai simular o ambiente de um carrinho de compras(Aqui usado Html, css, javascript, Python com Flask

3 - Integracao do repositorio github com o Vercel. O vercel vai servir para hospedar a nossa aplicacao Flask. O github action vai integrar nativamente com o Vercel, uma vez que todo push no branch principal
vai ativar o webhook do vercel e fazer o deplou para o ambiente de producao.

# Parte 1 - ASAAS

💳 Integração real com Asaas Payment API
- Primeiro crie seu cadastro no https://sandbox.asaas.com/
- Depois va no seu perfil -> Integracoes
- Apos isso va na Opcao Chaves de API -> Gerar Chave de API
- Apos isso uma chave de api sera gerada e ela sera usada no Flask/Python no lugar do seu ACCESS_TOKEN
- Outras funcionalidades como receber dinheiro real so fica disponivel apos envio de documentos e analise da empresa

<img width="1857" height="633" alt="image" src="https://github.com/user-attachments/assets/2f1dadf2-1c3e-42f6-a4e1-4eef228de772" />

# Parte 2 - Projeto Base com tecnologias da Web e Python

🛒 O proheto se resume a: Carrinho de compras com nome, quantidade, valor, subtotal e link de pagamento. Alem de adicao e remocao do produtos. Redirecionamento apos falha ou sucesso da compra.

📁 Estrutura do Projeto

<img width="227" height="270" alt="image" src="https://github.com/user-attachments/assets/8471da14-dca6-4ed5-999b-0bfef54e8f51" />


🧰 Tecnologias Utilizadas

Python 3.10+

Flask(Requests + render template + Redirect + os)

Asaas API (Payments)

HTML + CSS + JavaScript

Vercel (Deploy + Hospedagem com link criado por eles)

## ⚙️ Instalação Local

1️⃣ Clonar o repositório
git clone https://github.com/SEU_USUARIO/microservices-babystore.git

cd microservices-babystore

Depois rodar o comando do Docker Compose para subir localmente:
```
docker-compose up --build
```

2️⃣ Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar variável de ambiente

Crie um arquivo .env (opcional) ou exporte:

Linux/macOS:

export ASAAS_ACCESS_TOKEN="seu_token_aqui"


Windows:

setx ASAAS_ACCESS_TOKEN "seu_token_aqui"

## 🔑 Integração com Asaas

A aplicação utiliza a rota de criacao de Link de Pagamentos:

POST https://api-sandbox.asaas.com/v3/paymentLinks



<img width="1838" height="939" alt="image" src="https://github.com/user-attachments/assets/654669a5-0854-40e3-bc6e-26765843c5e5" />

Para fazer essa integracao no Python basta seguir o codigo abaixo:


```python
import requests

url = "https://api-sandbox.asaas.com/v3/paymentLinks"

payload = {
    "billingType": "CREDIT_CARD",
    "chargeType": "INSTALLMENT",
    "maxInstallmentCount": 3,
    "name": "store",
    "value": 100
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "access_token": "ACCESS_TOKEN_AQUI"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```


Enviando:

Nome do produto

Subtotal

Quantidade

Número de parcelas

URL de callback para sucesso

Tipo de cobrança (CREDIT_CARD)

O backend então:

Recebe dados do formulário

Faz POST para o Asaas

Pega data.url

Redireciona o usuário automaticamente

## 🖼️ Interface

A página principal (baby.html) contém:

Cabeçalho com tema de baby store(somente carrinho de compras

Formulário de produtos

Carrinho com reset automático

Botão para finalizar compra

Estética moderna, cores pastéis e ícones suaves


<img width="1194" height="564" alt="image" src="https://github.com/user-attachments/assets/5107c25c-7bdb-463d-80cf-2a36a86e8b96" />


🛑 Possíveis Erros
❗ Token inválido

Verifique variável ASAAS_ACCESS_TOKEN

❗ CORS ou redirecionamento bloqueado

Considere colocar successUrl autorizado no painel do Asaas

❗ Falha ao gerar pagamento

Verifique se o valor é decimal válido

Verifique parcelas ≤ maxInstallmentCount permitido pelo Asaas

# Parte 3 - Vercel para hospedar e deploy do projeto integrado com o Github
🌐 — Conectar GitHub ao Vercel

Acesse https://vercel.com
 e faça login (ou crie conta).

Clique em New Project → Import Git Repository.

Selecione seu repositório flask-hello-vercel do GitHub (conceda permissões).

No passo de configuração do projeto review, normalmente não precisa mudar nada (Vercel detecta vercel.json).

Clique Deploy.

O Vercel fará install (pip install -r requirements.txt) e build. Quando terminar, terá a URL pública do deploy.
Apos isso modifique o projeto de acordo com as suas preferencias e pronto. Sempre que fizer um push para a branch principal do projeto
ele vai fazer o deploy para o projeto

Ou voce pode criar um projeto a partir de um template como na figura abaixo. Assim ja criar um projeto pre configurado e basta modifica-lo:

<img width="1686" height="803" alt="image" src="https://github.com/user-attachments/assets/e1642801-ecd1-4a88-a18e-48ed5f8ee8ce" />

Nesse caso usamos o Flask Hello World e apenas modificamos com o codigo que o Assas Link De Pagamento gerou.
Apos isso fizemos a integracao do codigo HTML, CSS, Javascript com o codigo Python e Flask.


🔐 Uso de variáveis de ambiente para o access token
- Crie sua variavel de ambiente no Vercel para seu access token nao ficar exposto, ja que se trata de um repositorio public


🌐 Deploy no Vercel
1️⃣ Arquivos obrigatórios:

✔ vercel.json
✔ requirements.txt
✔ app.py

2️⃣ Definir variável de ambiente no painel da Vercel:

Vercel Dashboard → Project → Settings → Environment Variables

Chave: ASAAS_TOKEN


Valor: seu_token_do_asaas


OBS: Colocar agora as fotos do SandBox do Assas funcionando com o pagamento do cartao e tambem cenario de erro
e cenario pos comprar quando redireciona

OBS: colcoar tbm a tela de Cobrancas do ASAAS para mostrar todas as cobrancas feitas com cartao de credito


