from flask import Flask, request
from pymessenger.bot import Bot
import random

app = Flask(__name__)
ACESS_TOKEN ='EAADVCEQ2GEUBAGSxUKZAF11ZCjSOotllZArqJhHDuuzSpWRhvyLwZAiW0vfSxhoAZC5ZCDUNicKHhlCUwid7bbuQLsGRF7AOCJsMvVaHVV6Rbt6jiPxfclINLZAaEN2xSQxpfoedAdPZAPQPZCf4ToupLCCpDDcPHf9PHvZC2K21TNrQZDZD'

VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])


def recieve_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    if message['message'].get('attachments'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def get_message():
    sample_responses = ['Okaeri!', 'Hallo', 'Olá']
    return random.choice(sample_responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return 'sucess'

if __name__ == '__main__': app.run()