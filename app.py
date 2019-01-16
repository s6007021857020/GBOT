# from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# app = Flask(__name__)
#
# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#
# english_bot.set_trainer(ChatterBotCorpusTrainer)
# english_bot.train("chatterbot.corpus.thai")
#
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(english_bot.get_response(userText))
#
#
# if __name__ == "__main__":
#     app.run()

from flask import Flask, request, abort

app = Flask(__name__)

# url http://127.0.0.1:5000/?msg=asd
@app.route('/', methods=['GET'])
def webhook():
    if request.method == 'GET':
        msg = request.args.get('msg')
        print('GET: ' + msg)
        return '', 200
    elif request.method == 'POST':
        msg = request.args.get('msg')
        print('POST: ' + msg)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
