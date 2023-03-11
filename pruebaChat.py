import openai

#Definimos Key de OpenAI
openai.api_key = "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";

#Def de prueba para respuestas 
def ask_gpt(prompt, num_responses):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=num_responses, stop=None, temperature=0.5
    )
    response_text = str(response.choices[0].text.strip())
    return response_text

def main():
    #Prueba de repuestas
    message = "Resumen de la Gerra de Cenepa";
    respuesta = ask_gpt(message, 1)
    message += "\n"+ str(respuesta)
    print(message)

main()