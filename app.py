from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

# 🔥 Mensagens gerais (para fotos comuns)
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
    "Deixa eu fazer as coisas certas dessa vez..?",
    "saudades do seu jeito de Ioda...xD",
    "quem ve essas fotos nem imagina a mente do palhaço...",
    "Em 1000 vidas, eu escolheria a Karla em todas elas...",
    "Seu sorriso e sua risada são as melhores coisas do muuundo",
    "Você é o Jardim mais lindo do mundo...",
    "Saudade que não cabe no peito",
    "Você é a pessoa mais incrível de todo o mundo, K"
]

# 💌 Mensagens específicas por imagem
mensagens_especificas = {
    "casamento.jpg": "e eu nem sabia que esse era um dos dias mais felizes da minha vida...",
    "aniversario.jpg": "Eu pagaria rios de dinheiro para voltar nesse dia, nesse momento...",
    "me olha.jpg": "Seu sorriso quando vc me pegava te observando..."
}

# 🔁 Função reutilizável (boa prática)
def escolher_conteudo():
    try:
        imagens = os.listdir("static")
        imagens = [img for img in imagens if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        imagem = random.choice(imagens) if imagens else None
    except:
        imagem = None

    if imagem in mensagens_especificas:
        mensagem = mensagens_especificas[imagem]
    else:
        mensagem = random.choice(mensagens)

    return imagem, mensagem

# 🏠 Página principal
@app.route("/")
def home():
    imagem, mensagem = escolher_conteudo()
    return render_template("index.html", mensagem=mensagem, imagem=imagem)

# 🔄 Rota para trocar sem reload
@app.route("/proxima")
def proxima():
    imagem, mensagem = escolher_conteudo()
    return jsonify({
        "imagem": imagem,
        "mensagem": mensagem
    })

# 🚀 Rodar local
if __name__ == "__main__":
    app.run(debug=True)