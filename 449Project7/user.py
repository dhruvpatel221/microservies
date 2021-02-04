import flask, json, sqlite3, werkzeug.security
from flask import request, jsonify,g
import pugsql
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.apps import custom_app_context as pwd_context
from flask_api import status

app = flask.Flask(__name__)
app.config.from_envvar('APP_CONFIG')

#initialize query
queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])

@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries.engine.raw_connection()
        with app.open_resource('project.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


#https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"emanuel","email":"e@g.com","password":"python"}' http://127.0.0.1:5000/createUser
@app.route('/createUser', methods=['POST'])
def createUser():
        #implement this
         username = request.json.get('username')
         email = request.json.get('email')
         password = request.json.get('password')
         #created hashed password
         passwordHash = generate_password_hash(password, "sha256")

         queries.createUser(username=username,email=email,password=passwordHash)
         #created =('INSERT INTO user("username","email","password") VALUES ("dd","obdd@g.com","idk");')
         return f'User created', status.HTTP_201_CREATED


#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"emanuel","password":"python"}' http://127.0.0.1:5000/authenticateUser
@app.route('/authenticateUser', methods=['POST'])
def authenticateUser():
    #create variables
    username = request.json.get('username')
    password = request.json.get('password')

    userPass = queries.authenticateUser(username=username)
    hashedPassword = userPass.get('password')
    if (len(userPass.keys()) == 0):
          return  jsonify(message=username + ' was not found'),status.HTTP_404_NOT_FOUND
    if check_password_hash(hashedPassword, password):
        return jsonify(message=username + ' was authenticated successfully.'), status.HTTP_202_ACCEPTED
    else:
        return jsonify(message=username + ' password incorrect'), status.HTTP_401_UNAUTHORIZED

#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"name","follower":"name"}' http://127.0.0.1:5000/addFollower
@app.route('/addFollower', methods=['POST'])
def addFollower():
        username = request.json.get('username')
        follower = request.json.get('follower')

        queries.addFollower(username=username,follower=follower)
        #INSERT INTO userfollower(username, follower) VALUES (:username, :follower)
        return username + ' is now following ' + follower, status.HTTP_201_CREATED

#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"name","follower":"name"}' http://127.0.0.1:5000/removeFollower
@app.route('/removeFollower', methods=['POST'])
def removeFollower():
    username = request.json.get('username')
    follower = request.json.get('follower')

    # delete user from db
    queries.removeFollower(username=username, follower=follower)

    # DELETE from userfollower where username= :username and follower = :follower;
    return 'removed ' + follower, status.HTTP_200_OK

@app.route('/', methods=['GET'])
def home():
    return "<h1>Project 2></h1> <p> This is a user microservice </p>"
