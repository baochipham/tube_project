from flask import Flask, render_template
from trial_3 import delay_tweets
app = Flask(__name__)


@app.route('/') #routing
def home():
    tweets = delay_tweets()
    return render_template('tweet_embedder.html', tweets=tweets)
    #return 'work in progress'

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/show/<tube_line>')
def show(tube_line):
    return 'Showing delays for {}'.format(tube_line)

app.run(debug=True)