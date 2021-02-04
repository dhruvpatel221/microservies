import flask
from flask import request, jsonify
from flask_api import status
from datetime import datetime
import pugsql

app = flask.Flask(__name__)
app.config.from_envvar('APP_CONFIG')


queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])


@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries.engine.raw_connection()
        with app.open_resource('project.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#change "name" before trying curl command
#curl -i -X GET -H "Content-Type: application/json" -d '{"username":"name"}' http://127.0.0.1:8000/getUserTimeline
@app.route('/getUserTimeline', methods=['GET'])
def getUserTimeline():
    username = request.json.get('username')
    d = queries.getHomeTimeline(username=username)
    return jsonify(list(d)), status.HTTP_200_OK

#curl http://127.0.0.1:8000/getPublicTimeline
@app.route('/getPublicTimeline', methods=['GET'])
def getPublicTimeline():
    tweets = queries.getPublicTimeline()
    return jsonify(list(tweets)), status.HTTP_200_OK

#curl -i -X GET -H "Content-Type: application/json" -d '{"username":"name"}' http://127.0.0.1:8000/getHomeTimeLine
@app.route('/getHomeTimeLine', methods=['GET'])
def getHomeTimeline():
    username = request.json.get('username')
    recentTweets = queries.getHomeTimeline(username=username)
    return jsonify(list(recentTweets)), status.HTTP_200_OK

#curl -i -X GET -H "Content-Type: application/json" -d '{"tweet":"yourTweet","username":"name"}' http://127.0.0.1:8000/postTweet
@app.route('/postTweet', methods=['POST'])
def postTweet():
    username = request.json.get('username')
    tweet = request.json.get('tweet')
    queries.postTweet(tweet=tweet, username=username)
    return jsonify(username + " Tweeted: " + tweet), status.HTTP_201_CREATED

@app.route('/', methods=['GET'])
def home():
    return "<h1>CPSC 449 PROJECT 2</h1><p>Back-end microservices project for a microblogging service similar to Twitter.</p>"
