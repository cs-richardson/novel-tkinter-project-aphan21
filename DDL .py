DROP TABLE IF EXISTS ConsumerBuysNovel;
DROP TABLE IF EXISTS Consumer;
DROP TABLE IF EXISTS Novel;
DROP TABLE IF EXISTS Writer;

CREATE TABLE Consumer
(
	ConsumerID TINYINT NOT NULL,
	DOB DATE VARCHAR(10),
	Occupation VARCHAR(20),
	Address VARCHAR(40) NOT NULL,
	CreditCardNumber INT(16) NOT NULL,
	ConsumerName VARCHAR(30) NOT NULL,
	PRIMARY KEY (ConsumerID)
);
CREATE TABLE Writer
(
	WriterID TINYINT NOT NULL,
	Nationality VARCHAR(20),
	Gender VARCHAR(1),
	WriterName VARCHAR(20) NOT NULL,
	PRIMARY KEY (WriterID)
);
CREATE TABLE Novel
(
	NovelID TINYINT NOT NULL,
	Genre VARCHAR(25),
	Title VARCHAR(50) NOT NULL,
	Price INT(6) NOT NULL,
	Publisher VARCHAR(20),
	WriterID TINYINT NOT NULL,
	PRIMARY KEY (NovelID),
	FOREIGN KEY (WriterID) REFERENCES Writer(WriterID)
);
CREATE TABLE ConsumerBuysNovel
(
	ConsumerID TINYINT NOT NULL,
	NovelID TINYINT NOT NULL,	
	Price INT(6) NOT NULL,	
	PRIMARY KEY (ConsumerID, NovelID)
	FOREIGN KEY (ConsumerID) REFERENCES Consumer(ConsumerID)
	FOREIGN KEY (NovelID) REFERENCES Novel(NovelID)
);
INSERT INTO Consumer (ConsumerID, DOB, Occupation, Address, CreditCardNumber, ConsumerName) VALUES (1096254730, "10/17/2000", "Lawyer", "1010 Toddy St Santa Ana, CA", 1400961170004321, "Eden Mcguire");
INSERT INTO Consumer (ConsumerID, DOB, Occupation, Address, CreditCardNumber, ConsumerName) VALUES (1234567890, "9/3/1998", "Psychologist", "73 St John Riverside Residence, Sacramento, CA", 1268914376503269, "Jenna O'Brien");
INSERT INTO Consumer (ConsumerID, DOB, Occupation, Address, CreditCardNumber, ConsumerName) VALUES (4422668850, "7/1/1978", "Surgeon", "3789 Loyola Royal Compound, Chicago, IL ", 1086579412310055, "Michael O'Haire");

INSERT INTO Writer (WriterID, Nationality, Gender, WriterName) VALUES (2345098713, "British", "M", "Christian Anderson");
INSERT INTO Writer (WriterID, Nationality, Gender, WriterName) VALUES (9182736450, "German", "F", "Alexandra Walker");
INSERT INTO Writer (WriterID, Nationality, Gender, WriterName) VALUES (3376498105, "Vietnamese", "M", "Hoang Hai");

INSERT INTO Novel (NovelID, Genre, Title, Price, Publisher, WriterID) VALUES (1700961378, "Science Fiction", "Avatar", 43, "Pearson", 2345098713);
INSERT INTO Novel (NovelID, Genre, Title, Price, Publisher, WriterID) VALUES (7654321890, "Horror", "Dancing in the Dark", 85, "McMillan", 9182736450);
INSERT INTO Novel (NovelID, Genre, Title, Price, Publisher, WriterID) VALUES (1358679240, "Action", "Rivalry", 70, "Adam & Eva", 3376498105);

INSERT INTO ConsumerBuysNovel (ConsumerID, NovelID, Price) VALUES (1096254730, 1700961378, 43);
INSERT INTO ConsumerBuysNovel (ConsumerID, NovelID, Price) VALUES  (1234567890, 7654321890, 85);
INSERT INTO ConsumerBuysNovel (ConsumerID, NovelID, Price) VALUES (4422668850, 1358679240, 70);
