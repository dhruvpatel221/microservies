-- :name createUser :insert
INSERT INTO user(username,email,password) VALUES (:username, :email, :password);
