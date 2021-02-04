-- :name postTweet :insert
INSERT INTO usertweet(tweet, tweettime, username) VALUES (:tweet,  datetime('now'), :username);
