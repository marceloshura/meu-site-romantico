from flask import Flask, render_template
import random
import os

app = Flask(__name__)

mensagens = [
    "Você é sempre a melhor parte do meu dia, K ❤️",
    "Você é a mulher da minha vida, Dona K",
    "Penso em você todos os dias...",
    "Eu escolheria a Karla R.P. mil vezes em mil vidas",
    "Seu sorriso e sua risada são as melhores coisas do muuundo",
    "Você é o Jardim mais lindo do mundo...",
    "Saudade que não cabe no peito",
    "Você é a pessoa mais incrível de todo o mundo, K"
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