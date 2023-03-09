import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Definir una función para el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot de ejemplo.")

# Definir una función para el comando /ayuda
def ayuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Puedo ayudarte con lo que necesites.")

# Definir una función para manejar mensajes
def manejar_mensaje(update, context):
    mensaje_texto = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text="Has escrito: " + mensaje_texto)

# Definir la función principal
def main():
    # Crear una instancia del objeto Updater y pasarle el token del bot
    updater = Updater(token='6254161278:AAFBRMviOF-5k_ph-MGPdGbiX2UC41Iib1w', use_context=True)

    # Obtener el objeto dispatcher para registrar los manejadores
    dispatcher = updater.dispatcher

    # Registrar los manejadores de comando
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ayuda", ayuda))

    # Registrar el manejador de mensajes
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, manejar_mensaje))

    # Iniciar el bot
    updater.start_polling()

    # Ejecutar el bot hasta que se presione Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
