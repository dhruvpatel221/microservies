BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"username"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("username")
);
DROP TABLE IF EXISTS "userfollower";
CREATE TABLE IF NOT EXISTS "userfollower" (
	"username"	TEXT NOT NULL,
	"follower"	TEXT NOT NULL,
	FOREIGN KEY("follower") REFERENCES "user"("username"),
	FOREIGN KEY("username") REFERENCES "user"("username")
);
DROP TABLE IF EXISTS "usertweet";
CREATE TABLE IF NOT EXISTS "usertweet" (
	"tweet"	TEXT NOT NULL,
	"tweettime"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	FOREIGN KEY("username") REFERENCES "user"("username")
);
INSERT INTO "user" ("username","email","password") VALUES ('dhruv','dhruv@g.com','dhruv2323');
INSERT INTO "user" ("username","email","password") VALUES ('a','qwqw@g.com','qweocdsdc');
INSERT INTO "user" ("username","email","password") VALUES ('b','hiuhi@g.com','jhiugv');
INSERT INTO "user" ("username","email","password") VALUES ('c','ojkb@g.com','bvjhv');
INSERT INTO "user" ("username","email","password") VALUES ('d','hbb@g.com','biub');
INSERT INTO "user" ("username","email","password") VALUES ('e','e@g.com','cwdcwec');
INSERT INTO "user" ("username","email","password") VALUES ('dd','obdd@g.com','idk');
INSERT INTO "user" ("username","email","password") VALUES ('f','off@g.com','idk');
INSERT INTO "user" ("username","email","password") VALUES ('ppl','ss@g.com','sha256$eEdxy3fs$52cd32171b9e67b64c2279f20a647177f0e75514fb9cd219ffb94384aff5f652');
INSERT INTO "user" ("username","email","password") VALUES ('ddl','ddss@g.com','sha256$l0YEs1Tt$b57746b40cdaf27d245a96b44289ffcb0d1ba6659d3c5aafcd0564a7f77f41be');
INSERT INTO "user" ("username","email","password") VALUES ('dhruvv','ddffss@g.com','sha256$y0stox4R$98fe277b9754cd91e16345899c7e47fbdb3c30f3ded33c35af4c113f6c888ed8');
INSERT INTO "user" ("username","email","password") VALUES ('dhruvkumar','dss@g.com','sha256$btVrSxgL$b822ceb2e3c750989a0d4562693ce1b729023e55f5dde636d6d92cd810f97a30');
INSERT INTO "user" ("username","email","password") VALUES ('dhruvkumard','ifs@g.com','sha256$XRIRvK25$5d41e936f415a065a0c5579fb329fa977abb463a4f308abc8376ae0289c85e77');
INSERT INTO "user" ("username","email","password") VALUES ('emanuel11','eggg@g.com','sha256$Z2aBSKCm$c0312b254e2586b4f98ffd5aba2cfb769b2afb7696e1f519f7a33afc06e617fc');
INSERT INTO "user" ("username","email","password") VALUES ('emanuel','eFFg@g.com','sha256$vVJu3zuQ$c56ea9643e0eecd2d67afcf0b808a07024a286f92a6da95d785ef43232ead83b');
INSERT INTO "user" ("username","email","password") VALUES ('emanumhgmel','gregfe@g.com','sha256$aLl8nPdW$a34c033142ef9de6928ed00543f6b4d960360cec67b8ac8788bd1a5557436474');
INSERT INTO "user" ("username","email","password") VALUES ('edgar','edgar@gmail.com','sha256$hiqzTSul$ae883d5fdd52591697a20a80d1b6babce8b4aefa76706d539a71e0b97d26cfbd');
INSERT INTO "user" ("username","email","password") VALUES ('ed','ed@gmail.com','sha256$HdFuSYXV$4df47c3fd508ba5511fa1e0e191f88689bda59b2320a883acd181ab2611a9e7c');
INSERT INTO "user" ("username","email","password") VALUES ('silvia','silvia@g.com','sha256$xB55CJ4c$2731924f42624d1f4a646d7205c6d4126a59ea3d8ebd1d1c1e223c999ce46e36');
INSERT INTO "user" ("username","email","password") VALUES ('dog','dog@g.com','sha256$eVXHxbbM$e4606ff2a83a8c3f376bd29b39d739c5aa620aa49d59329350a1c3a6a9bbe0c9');
INSERT INTO "userfollower" ("username","follower") VALUES ('dhruv','a');
INSERT INTO "userfollower" ("username","follower") VALUES ('dhruv','b');
INSERT INTO "userfollower" ("username","follower") VALUES ('dhruv','c');
INSERT INTO "userfollower" ("username","follower") VALUES ('dhruv','e');
INSERT INTO "userfollower" ("username","follower") VALUES ('a','c');
INSERT INTO "userfollower" ("username","follower") VALUES ('a','e');
INSERT INTO "userfollower" ("username","follower") VALUES ('b','c');
INSERT INTO "userfollower" ("username","follower") VALUES ('e','dhruv');
INSERT INTO "userfollower" ("username","follower") VALUES ('c','dhruv');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi dhruv','2020-10-03 00:12:17','dhruv');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi E','2020-10-03 00:13:15','dhruv');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi C','2020-10-03 00:13:19','dhruv');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi B','2020-10-03 00:13:32','dhruv');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi a','2020-10-03 00:13:47','d');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi b','2020-10-03 00:13:54','a');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi c','2020-10-03 00:14:01','a');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi c','2020-10-03 00:14:05','e');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi a','2020-10-03 00:14:11','b');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi a','2020-10-03 00:14:23','b');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi e','2020-10-03 00:14:36','c');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi a','2020-10-03 00:34:18','e');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('bye bye','2020-10-03 00:52:43','d');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi dhruv','2020-10-09 04:08:36','a');
INSERT INTO "usertweet" ("tweet","tweettime","username") VALUES ('hi dhruv','2020-10-09 04:15:14','a');
COMMIT;
