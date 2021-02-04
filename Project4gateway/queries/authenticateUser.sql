-- :name authenticateUser :one
SELECT password FROM user WHERE username = :username;
