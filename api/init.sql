CREATE TABLE IF NOT EXISTS pickuplimes (
    limeID INTEGER PRIMARY KEY AUTOINCREMENT,
    pickuplime TEXT NOT NULL,
    source_link TEXT,
    source_text TEXT
);

CREATE TABLE IF NOT EXISTS tags (
    tag TEXT NOT NULL,
    limeID INTEGER NOT NULL,
    FOREIGN KEY (limeID) REFERENCES pickuplimes(id)
);

INSERT INTO pickuplimes(pickuplime) VALUES ("Go ahead, feel my shirt. It's made of boyfriend material!");
