import logging
import random
import time
import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from threading import Thread
from dotenv import load_dotenv

# === CARREGAR TOKEN DO .ENV ===
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# === CONFIGURAÇÕES ===
ID_DO_CHAT = -1006441158192  # Substitua pelo ID real do grupo
INTERVALO_MINUTOS = 10

mensagens = [
    "🚀 Token SATURNION já disponível! Aproveite enquanto está barato! 🔥 https://raydium.io",
    "💸 100x possível? Confira o gráfico e tire suas conclusões: https://dexscreener.com",
    "🌕 Vamos pra lua! Compre agora $SATURNION antes do FOMO chegar! 🚀",
    "🔥 Presale quase esgotada! Última chance! https://solscan.io/token/SEU_TOKEN",
]

# === SETUP DO BOT ===
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Pronto pra divulgar o token! 🚀")

def promo(update, context):
    msg = random.choice(mensagens)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('promo', promo))

def auto_post():
    while True:
        try:
            msg = random.choice(mensagens)
            bot.send_message(chat_id=ID_DO_CHAT, text=msg)
            print(f"[+] Mensagem enviada com sucesso.")
        except Exception as e:
            print(f"[!] Erro ao enviar mensagem: {e}")
        time.sleep(INTERVALO_MINUTOS * 60)

if __name__ == '__main__':
    Thread(target=auto_post).start()
    updater.start_polling()
    print("✅ Bot rodando e enviando mensagens...")
