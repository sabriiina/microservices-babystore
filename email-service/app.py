from flask import Flask, request, jsonify
import os
import aiosmtplib

app = Flask(__name__)

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

@app.route("/send", methods=["POST"])
async def send_email():
    data = request.json
    email = data["email"]
    mensagem = data["mensagem"]

    try:
        await aiosmtplib.send(
            message=mensagem,
            sender=SMTP_USER,
            recipients=[email],
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            username=SMTP_USER,
            password=SMTP_PASS
        )

        return jsonify({"status": "Email enviado!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route("/")
async def home():
    return "Email Service OK"
