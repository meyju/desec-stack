USE pdnslord;

ALTER TABLE users MODIFY username VARCHAR(64) NOT NULL DEFAULT '0';
ALTER TABLE users MODIFY password VARCHAR(128) NOT NULL DEFAULT '0';
