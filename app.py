from flask import Flask, request
import yagmail

app = Flask(__name__)

# Configurações do seu Gmail
EMAIL = "ferreiramateuss000@gmail.com"
SENHA = "jzkn nxia hecf ejcz"  # Use senha de app se tiver 2FA

# Inicia o cliente yagmail corretamente
yag = yagmail.SMTP(user=EMAIL, password=SENHA)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    nome = data.get("nome")
    email = data.get("email")

    print(f"📥 Recebido pedido de {nome} - {email}")

    assunto = "🎓 Seu acesso às videoaulas"
    conteudo = f"""
    Olá {nome}!

    Obrigado por adquirir o curso.

    Aqui está seu link de acesso:
    👉 https://seucurso.com/aulas

    Qualquer dúvida, estamos à disposição.

    — Equipe Matheus Ferreira
    """

    try:
        yag.send(to=email, subject=assunto, contents=conteudo)
        return {"status": "sucesso", "mensagem": f"E-mail enviado para {email}"}, 200
    except Exception as e:
        print("❌ Erro ao enviar e-mail:", e)
        return {"status": "erro", "mensagem": str(e)}, 500

@app.route('/ping')
def ping():
    return "✅ Online", 200

if __name__ == '__main__':
    app.run(port=5000)
