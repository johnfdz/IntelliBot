import requests

# Especifica el token del bot y la URL base de la API de Telegram Bot
bot_token = '6254161278:AAFBRMviOF-5k_ph-MGPdGbiX2UC41Iib1w'
api_base_url = f'https://api.telegram.org/bot{bot_token}'

# Especifica la URL pública de tu servidor y la ruta a tu script de bot
webhook_url = ''

# Envía una solicitud setWebhook a la API de Telegram Bot
response = requests.post(f'{api_base_url}/setWebhook', data={'url': webhook_url})

# Verifica si la solicitud se realizó correctamente
if response.ok:
    print('Webhook configurado correctamente')
else:
    print(f'Error al configurar el webhook: {response.content}')