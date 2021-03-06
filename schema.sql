CREATE TABLE IF NOT EXISTS USER(
   ID              INTEGER    PRIMARY KEY AUTOINCREMENT,
   LOGIN           CHAR(50)    NOT NULL,
   PASSWORD        CHAR(50)    NOT NULL,
   LAST_LOGIN      DATETIME DEFAULT NULL,
   LAST_UPDATE    DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS RANKING(
     ID INTEGER    PRIMARY KEY AUTOINCREMENT,
     USERID        INTEGER,
     GAME_TYPE     CHAR(50) NOT NULL,
     WIN           INT      DEFAULT 0,
     LOST          INT      DEFAULT 0,
     DRAW          INT      DEFAULT 0,
     LAST_UPDATE   DATETIME DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (USERID) REFERENCES USER(ID),
     FOREIGN KEY (GAME_TYPE) REFERENCES GAME_TYPE(ID)
);
