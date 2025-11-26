from flask import Flask, request, jsonify
import smtplib
import os

app = Flask(__name__)

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

@app.route("/send", methods=["POST"])
def send_email():
    data = request.json
    email = data["email"]
    mensagem = data["mensagem"]

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.sendmail(SMTP_USER, email, mensagem)

        return jsonify({"status": "Email enviado!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/")
def home():
    return "Email Service OK"
