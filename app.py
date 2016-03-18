from flask import Flask, render_template, request, redirect, url_for
import main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getTweet/<name>', methods=['GET'])
def getTweets(name):
    #person = request.form['twitter_name']
    #run script from here
    tweet = main.do(name)
    #return redirect(url_for('returnTweet', tweet = tweet))
    return tweet

@app.route('/tweet/<tweet>')
def returnTweet(tweet):
    return tweet


if __name__ == '__main__':
    app.debug = True
    app.run(port = 8000)
