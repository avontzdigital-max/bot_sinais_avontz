from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from datetime import datetime, timedelta
import random
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está rodando!"

def run_web():
    app.run(host="127.0.0.1", port=8080)

threading.Thread(target=run_web, daemon=True).start()

# 🔹 Configuração do Bot
API_ID = 29530163
API_HASH = "6066497fd46d35ea3dac9a179e27047b"
BOT_TOKEN = "7871641813:AAGvgNQpRvWuM0N7BXHPEqhTiEKoIK9DxMo"

# 🔹 Canal onde os sinais serão enviados
CHANNEL_ID = "@Avontzzp"

# 🔹 Caminhos das pastas de imagens
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PG_PATH = os.path.join(BASE_PATH, "Figurinhas Slots", "PG")
PP_PATH = os.path.join(BASE_PATH, "Figurinhas Slots", "PP")
JILI_PATH = os.path.join(BASE_PATH, "Figurinhas Slots", "jili")
JDB_PATH = os.path.join(BASE_PATH, "Figurinhas Slots", "jdb")

# 🔹 Jogos disponíveis com suas respectivas imagens
jogos = {
    # PG Soft Games
    "Fortune Snake 🐍": {
        "bet_min": 0.30,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "fortune-snake-p-g-soft.png"),
        "pasta": "PG"
    },
    "Fortune Mouse 🐹": {
        "bet_min": 0.50,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "65169f383ffff.png"),
        "pasta": "PG"
    },
    "Fortune Tiger 🐯": {
        "bet_min": 0.40,
        "bet_max": 5.0,
        "imagem": os.path.join(PG_PATH, "65169e4a15051.png"),
        "pasta": "PG"
    },
    "Gates of Olympus ⚡": {
        "bet_min": 0.20,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532a10e70f6b.png"),
        "pasta": "PP"
    },
    "Fortune Dragon 🐉": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "65dae7e5846fb.png"),
        "pasta": "PG"
    },
    "Fortune Gems 💎": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6533cff409b19.png"),
        "pasta": "PG"
    },
    "Fortune OX 🐂": {
        "bet_min": 0.50,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "65169ea36ddba.png"),
        "pasta": "PG"
    },
    "Double Fortune 🎎": {
        "bet_min": 0.30,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a22178564.png"),
        "pasta": "PG"
    },
    "Jackpot Joker 🎰🃏": {
        "bet_min": 0.20,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a6d54c48b.png"),
        "pasta": "PG"
    },
    "Fortune Gems 2 💎": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a247ed76.png"),
        "pasta": "PG"
    },
    "PartyStar 🐇": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a3d82c4308.png"),
        "pasta": "PG"
    },
    "Big Bass Splash 🎣": {
        "bet_min": 0.10,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532a9d00297.png"),
        "pasta": "PP"
    },
    "Cash Mania 💰": {
        "bet_min": 0.50,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532a921295.png"),
        "pasta": "PP"
    },
    "Wild Bandito 💀": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a6e20897f.png"),
        "pasta": "PG"
    },
    "Master Joker 🃏": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516ac992ca8.png"),
        "pasta": "PG"
    },
    "Lucky Neko 😺": {
        "bet_min": 0.50,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a5806d6ba.png"),
        "pasta": "PG"
    },
    "Aztec Gems Deluxe 🍃": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a31148733.png"),
        "pasta": "PG"
    },
    "Rio Fantasia 🐦‍🔥": {
        "bet_min": 0.50,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a4053883.png"),
        "pasta": "PG"
    },
    "Lucky Piggy 🐷": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a36806ba.png"),
        "pasta": "PG"
    },
    "Super Market Spree 🛒": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a864ec48b.png"),
        "pasta": "PG"
    },
    "Fortune Pig 🐷": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a52a5bf7.png"),
        "pasta": "PG"
    },
    "Piggy Gold 🐷": {
        "bet_min": 0.40,
        "bet_max": 400.0,
        "imagem": os.path.join(PG_PATH, "6516a4d59e0b.png"),
        "pasta": "PG"
    },
    # Pragmatic Play Games
    "Sweet Bonanza 🍭": {
        "bet_min": 0.20,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532b6c45e5e7.png"),
        "pasta": "PP"
    },
    "Fruit Party 🍓": {
        "bet_min": 0.20,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532a27e80541.png"),
        "pasta": "PP"
    },
    "Sugar Rush 🧁": {
        "bet_min": 0.20,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532a79c1df4fb.png"),
        "pasta": "PP"
    },
    "The Dog House 🐕": {
        "bet_min": 0.20,
        "bet_max": 400.0,
        "imagem": os.path.join(PP_PATH, "6532a490c0b308.png"),
        "pasta": "PP"
    },
    # JILI Games
    "Lucky Coming 🍀": {
        "bet_min": 0.10,
        "bet_max": 400.0,
        "imagem": os.path.join(JILI_PATH, "65330e7a2c91.png"),
        "pasta": "JILI"
    },
    "Golden Joker 🃏": {
        "bet_min": 0.10,
        "bet_max": 400.0,
        "imagem": os.path.join(JILI_PATH, "65334df602ee6.png"),
        "pasta": "JILI"
    },
    "Book of Gold 📚": {
        "bet_min": 0.10,
        "bet_max": 400.0,
        "imagem": os.path.join(JILI_PATH, "653342446459.png"),
        "pasta": "JILI"
    },
    # JDB Games
    "Fortune God 🏮": {
        "bet_min": 0.05,
        "bet_max": 400.0,
        "imagem": os.path.join(JDB_PATH, "65314dec50e4d.png"),
        "pasta": "JDB"
    },
    "Lucky Coming 🎊": {
        "bet_min": 0.05,
        "bet_max": 400.0,
        "imagem": os.path.join(JDB_PATH, "653150fb616.png"),
        "pasta": "JDB"
    },
    "Wu Kong 🐒": {
        "bet_min": 0.05,
        "bet_max": 400.0,
        "imagem": os.path.join(JDB_PATH, "65310dcab7c20.png"),
        "pasta": "JDB"
    }
}

# 🔹 Link de afiliação
LINKS_AFILIACAO = [
    "https://76x03.com/?pid=1007033839",
    "https://9276jogo.site/?pid=29056940",
    "https://78tt4.com/?pid=2347997525",
    "https://79b03.com/?pid=2372085789",
    "https://76k002.com/?pid=1531153975",
    "https://78n4.cc/?pid=2285388368",
    "https://85k885.com/?pid=2762981077",
    "https://67a01.com/?pid=2015249662",
]

link_index = 0 # usado para alternar de forma sequencial

# 🔹 Textos variados para os botões
TEXTOS_BOTOES = [
    "🚀 JOGUE AGORA",
    "💰 LUCRE AQUI",
    "🎯 APOSTAR AGORA",
    "🔥 COMEÇAR",
    "💎 GANHAR AGORA",
    "⚡ JOGAR",
    "🎪 DIVERSÃO AQUI",
    "🌟 INICIAR JOGO",
    "💸 FATURAR",
    "🎰 APOSTAR JÁ"
]

# Lista de vídeos como provas sociais
VIDEOS_PROVAS = [
    "https://t.me/SILVERCOPMTD/473",
    "https://t.me/SILVERCOPMTD/226",
    "https://t.me/SILVERCOPMTD/28",
    "https://t.me/SILVERCOPMTD/20",
    "https://t.me/SILVERCOPMTD/17",
    "https://t.me/SILVERCOPMTD/16",
    "https://t.me/SILVERCOPMTD/15",
    "https://t.me/SILVERCOPMTD/122",
    "https://t.me/SILVERCOPMTD/121",
    "https://t.me/SILVERCOPMTD/124",
    "https://t.me/SILVERCOPMTD/125",
    "https://t.me/SILVERCOPMTD/132",
    "https://t.me/SILVERCOPMTD/224",
    "https://t.me/Avontzz/10860",
    "https://t.me/Avontzz/10850",
    "https://t.me/Avontzz/10866",
    "https://t.me/Avontzz/10872",
    "https://t.me/Avontzz/10876",
    "https://t.me/Avontzz/10882",
    "https://t.me/Avontzz/10886",
    "https://t.me/Avontzz/10890",
    "https://t.me/Avontzz/10920",
    "https://t.me/Avontzz/10926",
    "https://t.me/Avontzz/10928",
    "https://t.me/Avontzz/10930",
    "https://t.me/Avontzz/10962",
    "https://t.me/SILVERCOPMTD/72",
    "https://t.me/SILVERCOPMTD/69",
    "https://t.me/Avontzz/28005",
    "https://t.me/Avontzz/28296",
    "https://t.me/Avontzz/28304",
    "https://t.me/Avontzz/28308",
]

app_bot = Client("bot_sinais",
                 api_id=API_ID,
                 api_hash=API_HASH,
                 bot_token=BOT_TOKEN)
# Mensagens automáticas que deixam o bot mais humanizado
MENSAGENS_HUMANIZADAS = [
    "🔍 Estamos monitorando novas oportunidades… aguarde sinais quentes!",
    "🎁 Já resgatou seu código gratuito de hoje? Corre antes que acabe!",
    "📢 A qualquer momento um jogo pode explodir… fique ligado!",
    "⚠️ Não jogue aleatório! Espere o próximo sinal validado pela equipe.",
    "🎲 Giramos por aqui e já estamos vendo padrões estranhos… atenção!",
    "💰 Tá rolando muitos saques hoje… se posicione!",
    "⏳ Já já mais um jogo validado, segura aí!",
    "🔥 Alerta! Plataforma aquecendo… mais uma oportunidade a caminho!",
    "📊 Análise em tempo real… possível entrada em breve!",
    "✅ Finalizando testes… próximo jogo pode vir com força!",
    "👀 Já viu os resultados anteriores? Confere lá no canal!",
    "🧨 Plataforma instável… ideal para pescaria rápida!",
    "🧠 Nosso time está cruzando dados… prepare-se!",
    "📈 Apostas menores também lucram! É só seguir as estratégias.",
    "🔐 Resgate seu bônus diário e fique pronto para os sinais!"
]

def calcular_bet(deposito):
    if deposito >= 50:
        return 5.00
    elif deposito >= 30:
        return 2.00
    elif deposito >= 20:
        return 1.00
    elif deposito >= 10:
        return 0.40
    else:
        return 0.20

def criar_botao_afiliacao():
    global link_index
    texto_botao = random.choice(TEXTOS_BOTOES)

    # Seleciona o link atual
    link_atual = LINKS_AFILIACAO[link_index]

    # Avança para o próximo link (modo circular)
    link_index = (link_index + 1) % len(LINKS_AFILIACAO)

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(texto_botao, url=link_atual)]
    ])


def gerar_mensagem(jogo, deposito, aposta):
    now = datetime.now()
    horario_sinal = now + timedelta(minutes=3)
    horario_formatado = horario_sinal.strftime("%H:%M")
    estrategia = "🔹 Automático 10x, Turbo ligado"
    nova_opcao = random.choice(list(jogos.keys()))
    
    # Emojis variados para deixar mais atrativo
    emojis_fire = ["🔥", "💥", "⚡", "🚀", "💎", "🎯"]
    emoji_escolhido = random.choice(emojis_fire)
    
    mensagem = f"""
{emoji_escolhido} **SINAL QUENTE - SLOTS** {emoji_escolhido}

⏰ **Hora Certa para Apostar!** Jogue **{jogo}** 
📅 **Horário recomendado**: {horario_formatado}
💰 **Depósito**: R$ {deposito}
🎯 **Aposta sugerida**: R$ {aposta}
📝 **Estratégia**: {estrategia}

💡 **Dica de Profissional**: Se os 10 giros forem positivos, aumente a aposta e jogue mais 10x. Caso contrário, tente **{nova_opcao}**.

🍀 **Boa sorte e bons lucros!** 🍀
"""
    return mensagem

async def enviar_sinais():
    while True:
        jogo_nome = random.choice(list(jogos.keys()))
        jogo_info = jogos[jogo_nome]
        deposito = random.choice([10, 20, 30, 50])
        aposta = calcular_bet(deposito)
        mensagem = gerar_mensagem(jogo_nome, deposito, aposta)
        
        try:
            # Verifica se a imagem existe
            if os.path.exists(jogo_info["imagem"]):
                # Envia a imagem do jogo com a mensagem e botão
                await app_bot.send_photo(
                    CHANNEL_ID,
                    jogo_info["imagem"],
                    caption=mensagem,
                    reply_markup=criar_botao_afiliacao()
                )
                print(f"✅ Sinal enviado para {jogo_nome}")
            else:
                # Se a imagem não existir, envia apenas o texto
                await app_bot.send_message(
                    CHANNEL_ID,
                    mensagem,
                    reply_markup=criar_botao_afiliacao()
                )
                print(f"⚠️ Sinal enviado para {jogo_nome} (sem imagem - arquivo não encontrado)")
            
            # Aguarda 30 segundos
            await asyncio.sleep(30)
            
            # Depois envia o vídeo de prova social
            video_escolhido = random.choice(VIDEOS_PROVAS)
            await app_bot.send_video(
                CHANNEL_ID,
                video_escolhido,
                caption="🎉 Olha os resultados! Quer aprender? Cola com a gente! 🚀"
            )
            print("📹 Prova social enviada!")
            
        except Exception as e:
            print(f"❌ Erro ao enviar mensagem: {e}")
        
        # Aguarda 5 minutos (300 segundos) antes do próximo sinal
        await asyncio.sleep(300)
async def enviar_mensagens_humanizadas():
    while True:
        try:
            mensagem = random.choice(MENSAGENS_HUMANIZADAS)
            await app_bot.send_message(CHANNEL_ID, mensagem)
            print(f"💬 Mensagem humanizada enviada: {mensagem}")
        except Exception as e:
            print(f"❌ Erro ao enviar mensagem humanizada: {e}")
        
        await asyncio.sleep(random.randint(180, 420))  # entre 3 e 7 minutos

async def main():
    print("🤖 Iniciando bot de sinais...")
    print(f"📁 Pasta base: {BASE_PATH}")
    print(f"📁 Pasta PG: {PG_PATH}")
    print(f"📁 Pasta PP: {PP_PATH}")
    print(f"📁 Pasta JILI: {JILI_PATH}")
    print(f"📁 Pasta JDB: {JDB_PATH}")
    
    async with app_bot:
        print("✅ Bot conectado com sucesso!")
        print(f"📢 Enviando sinais para: {CHANNEL_ID}")
        await asyncio.gather(
    enviar_sinais(),
    enviar_mensagens_humanizadas()
)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n🛑 Bot interrompido pelo usuário")
    except Exception as e:
        print(f"❌ Erro fatal: {e}")