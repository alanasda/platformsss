from flask import Flask, request
import yagmail
import os

app = Flask(__name__)

EMAIL = os.environ.get("EMAIL")
SENHA = os.environ.get("SENHA")

yag = yagmail.SMTP(EMAIL, SENHA)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    nome = data.get("nome")
    email = data.get("email")

    print(f"Recebido pedido de {nome} - {email}")

    assunto = "🎓 Seu acesso às videoaulas"
    conteudo = f"""
    Olá {nome}!

    Obrigado por adquirir o curso.

    Aqui está seu link de acesso:
    👉 https://seucurso.com/aulas

    Qualquer dúvida, estamos à disposição.

    — Equipe SeuNome
    """

    try:
        yag.send(to=email, subject=assunto, contents=conteudo)
        return {"status": "sucesso", "mensagem": f"E-mail enviado para {email}"}, 200
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
        return {"status": "erro", "mensagem": str(e)}, 500

@app.route('/ping')
def ping():
    return "pong", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
