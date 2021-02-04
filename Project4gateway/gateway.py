#

# Simple API gateway in Python

#

# Inspired by <https://github.com/vishnuvardhan-kumar/loadbalancer.py>

#

#   $ python3 -m pip install Flask python-dotenv

#



import sys, flask, requests, itertools

from itertools import cycle



from flask_api import status

from functools import wraps

from flask import request



app = flask.Flask(__name__)

app.config.from_envvar('APP_CONFIG')

users_stream = cycle(app.config['USERS'])

users = {'/createUser', '/authenticateUser', '/addFollower', '/removeFollower'}

timeline_stream = cycle(app.config['TIMELINES'])

timeline = {'/getUserTimeline', '/getPublicTimeline', '/getHomeTimeline', '/postTweet'}



def check_auth(username, password):

    response = requests.post(next(users_stream) + '/authenticateUser', json={'username': "emanuel", 'password':"python"})


    if response.status_code == 200:
        sys.stderr.write(str("----------------------i"))
        return True

    else:
        sys.stderr.write(str("hii"))
        return False



@app.errorhandler(404)



def route_page(err):

    # print(e.requests.url)

    try:

        domain, path = route_path(flask.request.path)

        response = requests.request(

            flask.request.method,

            # resource: https://stackoverflow.com/a/46176337

            domain+path,

            data=flask.request.get_data(),

            headers=flask.request.headers,

            cookies=flask.request.cookies,

            stream=True,

        )


        #Server will be removed form rotation if HTTP status code is 5xx

        if response.status_code >= 500:

                delete_server(domain,path)

        #Just for testing

        '''

        if response.status_code <= 500:

            if domain == 'http://localhost:5202':

                delete_server(domain,path)

            if domain == 'http://localhost:5102':

                delete_server(domain,path)

        '''
        #Authentication check
        if(path =='/authenticateUser'):
            if response.status_code != 202:
                return ('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})



    except requests.exceptions.RequestException as e:

        app.log_exception(sys.exc_info())

        return flask.json.jsonify({

            'method': e.request.method,

            'url': e.request.url,

            'exception': type(e).__name__,

        }), 503



    headers = remove_item(

        response.headers,

        'Transfer-Encoding',

        'chunked'

    )



    return flask.Response(

        response=response.content,

        status=response.status_code,

        headers=headers,

        direct_passthrough=True,

    )

#function to route path to idenify user and timeline service and to assign specific server in rotation

def route_path(route):

    if route in users:

        return next(users_stream),route



    elif route in timeline:

        return next(timeline_stream),route



    else:

        flask.abort(404, description="Resource not found")



def remove_item(d, k, v):

    if k in d:

        if d[k].casefold() == v.casefold():

            del d[k]

    return dict(d)

#Function to remove server in rotation

def delete_server(domain,path):

    if path in users:

        global users_stream

        app.config['USERS'].remove(domain)

        #sys.stderr.write(str(app.config['USERS'])) TESTING

        users_stream = cycle(app.config['USERS'])

    if path in timeline:

        global timeline_stream

        app.config['TIMELINES'].remove(domain)

        timeline_stream = cycle(app.config['TIMELINES'])
