import telegram, openai, json, requests

#Obtener mensajes /getUpdate
#Obtener datos del Bot /getMe
#Enviar Mensajes /sendMessage
with open('keys.json') as keys:
    datos = json.load(keys)
    print (datos['openai'])
    openai.api_key = datos['openai']
    token = datos['token']
    
    
#Definimos link de Telegram
link = (f'https://api.telegram.org/bot{token}/')

def getMe(link):
    response = requests.get(link + 'getMe')
    return response

def sendMessage(link, message, chat_id):
    request = requests.post(link + 'sendMessage',
                            data= {'chat_id' : chat_id, 'text' : message})
    if request.status_code == 200:
        print ('Sent message')
    else: 
        print ('Error sending message') 

def response(link, message):
    request = requests.get(link + 'getUpdates')
    data = json.loads(request.content)

def getUpdates(link):
    update = requests.get(link + 'getUpdates')
    data = json.loads(update.content)
    results = data['result']
    question = results[0]['message']['text']
    id = results[0]['message']['from']['id']
    response = ask_gpt(question, 1)
    print (response)
    sendMessage(link, response, id)


#Def de prueba para respuestas 
def ask_gpt(prompt, num_responses):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=num_responses, stop=None, temperature=0.5
    )
    response_text = str(response.choices[0].text.strip())
    return response_text

# Definir la función principal
def main():
    #Obtener actulizaciones de mensajes
    getUpdates(link)

    #Metodos Bot
    request = getMe(link)
    datos = json.loads(request.content)
    id = datos['result']['id']
    
    
#Llamado a la funcion Main
if __name__ == '__main__':
    main()
