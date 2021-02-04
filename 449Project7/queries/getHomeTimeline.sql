-- :name getHomeTimeline :many
SELECT tweet FROM usertweet  WHERE username IN (SELECT follower FROM userfollower WHERE username= :username) ORDER BY tweettime DESC LIMIT 25;
