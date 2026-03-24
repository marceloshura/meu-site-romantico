from flask import Flask, render_template
import random
import os

app = Flask(__name__)

mensagens = [
    "Você é a melhor parte do meu dia ❤️",
    "Penso em você o tempo todo",
    "Seu sorriso muda tudo",
    "Saudades de você",
    "Você é incrível"
]

@app.route("/")
def home():
    mensagem = random.choice(mensagens)

    try:
        imagens = os.listdir("static")
        imagens = [img for img in imagens if img.endswith(('.png', '.jpg', '.jpeg'))]
        imagem = random.choice(imagens) if imagens else None
    except:
        imagem = None

    return render_template("index.html", mensagem=mensagem, imagem=imagem)

if __name__ == "__main__":
    app.run(debug=True)