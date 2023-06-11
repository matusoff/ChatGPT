#install telebot for telegram API
import telebot
import openai

telegram_key = 'your key'
openai.api_key = 'your openai key'


bot = telebot.TeleBot(telegram_key)

@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, "Hi, I'm your ChatGPT bot. How can I help you? ")


@bot.message_handler(content_types=['text'])
def main(message):
    response = openai.Completion.create(
        engine='text-davinci-003', 
        prompt=message.text, 
        temperature=0.7, 
        max_tokens=100, 
        n=1, 
        stop=None,
        timeout=15 
    )

    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = 'Something went wrong'


    bot.send_message(message.chat.id, reply) 

bot.polling(none_stop=True)
