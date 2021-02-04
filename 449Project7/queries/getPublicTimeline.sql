-- :name getPublicTimeline :many
SELECT tweet from usertweet ORDER BY tweettime DESC LIMIT 25;
