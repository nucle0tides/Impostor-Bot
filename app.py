from flask import Flask, render_template, request, redirect, url_for
import main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getTweet/<name>', methods=['GET'])
def getTweets(name):
    tweet = main.do(name)
    return tweet

@app.route('/more/')
def more():
    return render_template('more.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port = 8000)
