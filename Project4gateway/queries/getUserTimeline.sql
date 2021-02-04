-- :name getUserTimeline :many
SELECT tweet FROM usertweet WHERE username = :username ORDER BY tweettime DESC LIMIT 25;
