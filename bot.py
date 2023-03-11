import telegram, openai, json, requests

#Definimos Key de OpenAI
openai.api_key = "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";

#Definimos Token de Telegram
token = '6254161278:AAFBRMviOF-5k_ph-MGPdGbiX2UC41Iib1w'

#Definimos link de Telegram
link = (f'https://api.telegram.org/bot{token}/')

def getMe(link):
    response = requests.get(link + 'getMe')
    return response
    

#Def de prueba para respuestas 
def ask_gpt(prompt, num_responses):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=num_responses, stop=None, temperature=0.5
    )
    response_text = str(response.choices[0].text.strip())
    return response_text

# Definir la función principal
def main():
    #Metodos Bot
    request = getMe(link)
    datos = json.loads(request.content)
    id = datos['result']['id']

    #Prueba de repuestas
    message = "Resumen de la Gerra de Cenepa";
    respuesta = ask_gpt(message, 1)
    message += "\n"+ str(respuesta)
    print(id)
    #print(message)
    
#Llamado a la funcion Main
if __name__ == '__main__':
    main()
