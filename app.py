from flask import Flask, render_template
import random
import os

app = Flask(__name__)

mensagens = [
    "Você é, sempre, a melhor parte do meu dia, K ❤️",
    "Você é a mulher da minha vida, Dona K",
    "Penso em você todos os dias...",
    "Eu não sou nada sem seu amor..",
    "saudades de cantar nossas músicas coladinhos...",
    "Seu novo perfume é maravilhoso...",
    "Me deixa te reconquistar?",
    "De flor mais linda para o jardim... Continua a mais linda do mundo",
    "Meu mundo sem você é o universo mais triste do mundo!",
    "Quero ser o meu melhor ao lado da melhor pessoa do mundo...",
    "Dona K, eu ainda te amo...",
    "Quando você melhorar, sai comigo?",
    "Eu queria tomar um banho de chuva contigo, K",
    "Deixa eu fazer as coisas certas dessa vez..? ",
    "saudades do seu jeito de Ioda...xD ",
    "quem ve essas fotos nem imagina a mente do palhaço...",
    "Em 1000 vidas, eu escolheria a Karla em todas elas...",
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