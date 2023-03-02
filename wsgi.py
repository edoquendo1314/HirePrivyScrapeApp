from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/email_webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return ('success', 200)
    else:
        abort(400)

class WebhookApp:
    async def call_webhook():
        return webhook()

if __name__ == '__main__':
    WebhookApp.run()