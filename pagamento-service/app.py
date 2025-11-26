from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

ASAAS_TOKEN = os.environ.get("ASAAS_TOKEN")
EMAIL_URL = os.environ.get("EMAIL_URL")  # chama o serviço de email

@app.route("/gerarlink", methods=["POST"])
def gerarlink():
    data = request.json
    
    payload = {
        "billingType": "CREDIT_CARD",
        "chargeType": "INSTALLMENT",
        "name": data["nome"],
        "value": data["subtotal"],
        "isAddressRequired": False,
        "maxInstallmentCount": data["parcelas"],
        "description": f"Compra de {data['quantidade']}x {data['nome']}",
        "callback": {
            "successUrl": "https://seusite.com/compracerta"
        }
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": ASAAS_TOKEN
    }

    response = requests.post("https://api-sandbox.asaas.com/v3/paymentLinks",
                             json=payload, headers=headers)
    data_response = response.json()

    # Erro → retorna erro para o cadastro-service
    if "errors" in data_response:
        return jsonify({"erro": data_response["errors"][0]["description"]}), 400

    # sucesso → envia email via micro serviço
    link_pagamento = data_response["url"]

    requests.post(f"{EMAIL_URL}/send", json={
        "email": "cliente@gmail.com",
        "mensagem": f"Seu link de pagamento: {link_pagamento}"
    })

    return jsonify({"link": link_pagamento})

@app.route("/")
def home():
    return "Pagamento Service OK"
