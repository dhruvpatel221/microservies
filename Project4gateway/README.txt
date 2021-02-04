Project: 4

Project Members:

-Dhruvkumar D Patel (dhruvdpatel212@csu.fullerton.edu)
-Emanuel carmona(emanuelcarmona714@gmail.com)
-Asmita (asmita.koirala@csu.Fullerton.edu)

We have made no changes to project 2

To run the service:
<<<<<<< HEAD
2)Run command to populate the database $ FLASK_APP=timelines flask init
=======
2) Run command $ FLASK_APP=timelines flask init (initialize the database)
>>>>>>> 503b35ab6c815b552c3b8e81749e05b8641a2785
3)Run command $ foreman start -m gateway=1,user=3,timelines=3


routes.cfg​ contains
"
TIMELINES = ['http://localhost:5200', 'http://localhost:5201', 'http://localhost:5202']
DATABASE_URL = 'sqlite:///project.db'
USERS = ['http://localhost:5100', 'http://localhost:5101', 'http://localhost:5102']

"
Procfile​ contains
"
#foreman start -m gateway=1,user=3,timelines=3
gateway: FLASK_APP=gateway flask run -p $PORT
user: env FLASK_APP=user.py flask run -p $PORT
timelines: env FLASK_APP=timelines.py flask run -p $PORT

"

TO TEST :
Users Service (running on 3 different Port)
1) curl -i -X POST -H "Content-Type: application/json" -d '{"username":"nameq12312","email":"email1231qq2@site.com","password":"password1"}' http://127.0.0.1:5000/createUser
2) curl -i -X POST -H "Content-Type: application/json" -d '{"username":"name12121112","email":"emai12312w22@site.com","password":"password1"}' http://127.0.0.1:5000/createUser
3 )curl -i -X POST -H "Content-Type: application/json" -d '{"username":"nameq123122","email":"email111d2@site.com","password":"password1"}' http://127.0.0.1:5000/createUser

TO TEST :
Timeline Service (running on 3 different Port)
1) curl -i -X GET -H "Content-Type: application/json" -d '{"username":"name"}' http://127.0.0.1:5000/getUserTimeline
2) curl -i -X GET -H "Content-Type: application/json" -d '{"username":"name"}' http://127.0.0.1:5000/getUserTimeline
3) curl -i -X GET -H "Content-Type: application/json" -d '{"username":"name"}' http://127.0.0.1:5000/getUserTimeline
