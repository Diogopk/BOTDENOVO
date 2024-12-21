import asyncio
from telegram import Bot
import schedule
import time
from datetime import datetime
import pytz


# Token do Bot fornecido pelo BotFather
TOKEN = '7674535361:AAHupIHd-MGp8kAg-eluXBrMSSbEzxyDilw'

# ID dos grupos para onde o bot enviará mensagens
GROUP_IDS = [-1002373652578,]  # Substitua pelos IDs dos seus grupos

# Mensagem que será enviada
MENSAGEM = "Bom dia, grupo! 🌞 Esta é uma mensagem automática."

# Definir o fuso horário (exemplo: Brasília, GMT-3)
FUSO_HORARIO = pytz.timezone('America/Sao_Paulo')

# Função para enviar mensagens (assíncrona)
async def enviar_mensagem():
    bot = Bot(token=TOKEN)
    for group_id in GROUP_IDS:
        await bot.send_message(chat_id=group_id, text=MENSAGEM)

# Função para rodar a tarefa de forma síncrona
def agendar_envio():
    print(f"Enviando mensagem às {datetime.now(FUSO_HORARIO).strftime('%H:%M:%S')}")
    asyncio.run(enviar_mensagem())

# Agendar o envio de mensagens
schedule.every().day.at("18:50").do(agendar_envio)  # Horário 1
schedule.every().day.at("18:52").do(agendar_envio)  # Horário 2
schedule.every().day.at("18:55").do(agendar_envio)  # Horário 3

# Loop para manter o script rodando
if __name__ == "__main__":
    print("Bot está rodando...")
    while True:
        schedule.run_pending()
        time.sleep(1)
