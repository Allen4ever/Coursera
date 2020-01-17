CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Zechariah', 25);
INSERT INTO Ages (name, age) VALUES ('Ewan', 21);
INSERT INTO Ages (name, age) VALUES ('Tabetha', 39);
INSERT INTO Ages (name, age) VALUES ('Airlie', 30);
INSERT INTO Ages (name, age) VALUES ('Mara', 19);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
