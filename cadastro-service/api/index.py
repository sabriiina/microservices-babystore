from flask import Flask, render_template, request, jsonify, redirect
import requests
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("baby.html")

@app.route("/gerarlink", methods=["POST"])
def gerarlink():
    nome = request.form.get("nome")
    quantidade = request.form.get("quantidade")
    valor = request.form.get("valor")
    subtotal = request.form.get("subtotal")
    produtos_json = request.form.get("produtos_json")
    parcelas = request.form.get("parcelas")

    # URL do Asaas
    url = "https://api-sandbox.asaas.com/v3/paymentLinks"

    payload = {
        "billingType": "CREDIT_CARD",
        "chargeType": "INSTALLMENT",
        "name": nome,
        "value": subtotal,
        "isAddressRequired": False,
        "maxInstallmentCount": parcelas,
        "description": f"Compra de {quantidade}x {nome}",
        "callback": {
            "successUrl": "https://flask-tito-baby.vercel.app//compracerta"
        }
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": os.environ.get("ASAAS_TOKEN")
    }

    # Faz a requisição
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    # Se der erro
    if "errors" in data:
        erro = data["errors"][0]["description"]
        return render_template("compraerrada.html", erro=erro)
        #return render_template("compraerrada.html")
        #return redirect("/compraerrada")


    # Pega o link de pagamento
    link_pagamento = data.get("url")

    # 🔥 REDIRECIONA PARA O LINK NA MESMA ABA
    return redirect(link_pagamento)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

# if __name__ == "__main__":
#     app.run()

# para poder rodar local
