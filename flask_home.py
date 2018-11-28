from flask import Flask, render_template
from trial import get_tweets
app = Flask(__name__)


@app.route('/') #routing
def home():
    tweets = get_tweets()
    return render_template('tweet_embedder.html', tweets=tweets)


app.run(debug=True)