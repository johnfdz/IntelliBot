import telegram, openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
'''
#Definimos Key de OpenAI
openai.api_key = "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";

#Def de prueba para respuestas 
def ask_gpt(prompt, num_responses):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=num_responses, stop=None, temperature=0.5
    )
    response_text = str(response.choices[0].text.strip())
    return response_text
'''
# Definir una función para el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot de ejemplo.")

# Definir una función para el comando /ayuda
def ayuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Puedo ayudarte con lo que necesites.")

#Definir una función para mensajes
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="He recibido tu mensaje: " + update.message.text)


# Definir una función para manejar mensajes
def manejar_mensaje(update, context):
    mensaje_texto = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text="Has escrito: " + mensaje_texto)

# Definir la función principal
def main():
    '''
    #Prueba de repuestas
    message = "Resumen de la Gerra de Cenepa";
    respuesta = ask_gpt(message, 1)
    message += "\n"+ str(respuesta)
    print(message)
    '''
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

#Llamado a la funcion Main
if __name__ == '__main__':
    main()
