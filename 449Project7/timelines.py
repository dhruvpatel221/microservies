import flask, redis
import sqlite3, time, datetime
from flask import request, jsonify, Flask
from werkzeug.exceptions import HTTPException, default_exceptions,  Aborter
from flask_api import status
import pugsql

from redis import Redis
from rq import Queue

# Import the time module to include some time delay in the application
import time


app = flask.Flask(__name__)
app.config.from_envvar('APP_CONFIG')
app.app_context().push()

queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])

# Make a connection of the queue and redis
r = redis.Redis()
q = Queue(connection=r)
q2 = Queue(connection=r)


@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries.engine.raw_connection()
        with app.open_resource('project.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Create a working task queue  
def task_handler(username,tweet):
    queries.postTweet(tweet=tweet, username=username)

    print("Task running")

    print("Task Complete")
    return jsonify(username + " Tweeted: " + tweet), status.HTTP_202_ACCEPTED    

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


#curl -i -X POST -H "Content-Type: application/json" -d '{"tweet":"yourTweet","username":"dhruv"}' http://127.0.0.1:8000/postTweet
@app.route('/postTweet', methods=['POST'])
def postTweet():
    username = request.json.get('username')
    tweet = request.json.get('tweet')
    #queries.postTweet(tweet=tweet, username=username)
    q.enqueue(task_handler,username,tweet)
    q2.enqueue(analytics,tweet)
    return jsonify(username + " Tweeted: " + tweet), status.HTTP_201_CREATED

#curl -i -X POST -H "Content-Type: application/json" -d '{"tweet":"yourTweet","username":"dhruv"}' http://127.0.0.1:8000/syncTweet
@app.route('/syncTweet', methods=['POST'])
def syncTweet():
    username = request.json.get('username')
    tweet = request.json.get('tweet')
    queries.postTweet(tweet=tweet, username=username)
    return jsonify(username + " Tweeted: " + tweet), status.HTTP_201_CREATED

def analytics(tweet):
    words = tweet.split()
    hashtag_words = []
    for hashtags in words:
        if '#' in hashtags:
            hashtag_words.append(hashtags)

    for hash_word in hashtag_words:
        r.zincrby ("top", 1, hash_word)

# curl http://127.0.0.1:8000/trending
@app.route('/trending', methods=['GET'])
def trending():
    trending_list = r.zrevrange('top', 0, 24, withscores=True)
    return jsonify(list(trending_list))



@app.route('/', methods=['GET'])
def home():
    return "<h1>CPSC 449 PROJECT 2</h1><p>Back-end microservices project for a microblogging service similar to Twitter.</p>"