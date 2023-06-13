#image generation from the text message

import requests

KEY = 'your key from openai'

def generate(message):
    url = 'https://api.openai.com/v1/images/generations'

    headers = {
        'Authorization': f'Bearer {KEY}',
        'Content-Type': 'application/json',
        }

    response = requests.post(url, json={"prompt": message}, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error:", response.text)


text = 'Porshe plus Tesla'

generate(text)
