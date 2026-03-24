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

    imagens = os.listdir("static")
    imagem = random.choice(imagens)

    return render_template("index.html", mensagem=mensagem, imagem=imagem)

if __name__ == "__main__":
    app.run(debug=True)