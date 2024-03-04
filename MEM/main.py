from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI

API = 'your API'
client = OpenAI(api_key=API)

def generate_response(text):
    response = client.completions.create(
        prompt=text,
        model='gpt-3.5-turbo-instruct'
    )

    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None
    
prompt = 'Write two lines of text to be used in a meme. The first line should go above an image, and the second line should go below, with a clear separation between them indicated by a specific symbol %%'
res= generate_response(prompt)
results = res.split('%%')


# Open image
img = Image.open('meme.jpg')

# Making an object ImageDraw for drawing a text
draw = ImageDraw.Draw(img)

top_text = results[0]
bottom_text = results[1]

draw.text((240, 70), top_text, (0, 0 , 0))
draw.text((240, 250), bottom_text, (0, 0 , 0))

img.save('meme2.jpg')
Image.open('meme2.jpg').show()
