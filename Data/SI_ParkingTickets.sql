CREATE DATABASE IF NOT EXISTS SIdb;
USE SIdb;
DROP TABLE IF EXISTS SItable;
CREATE TABLE SItable (
      ticket_id INT,
      SummonsNumber INT,
      IssueDate TEXT,
      ViolationCode INT,
      StreetCode1 INT,
      StreetCode2 INT,
      StreetCode3 INT,
      ViolationPrecinct INT,
      ViolationTime TEXT,
      ViolationCounty TEXT,
      ViolationFrontOpposite ENUM('F', 'O'),
      HouseNumber TEXT,
      StreetName TEXT,
      IntersectingSt TEXT,
      ticket_year INT,
      ticket_day INT,
      ticket_month INT,
      newdate INT,
      newtime INT,
      weekday INT,
      uniqueID BIGINT,
	  newhour INT,
      address TEXT
);

LOAD DATA LOCAL INFILE '/Users/marco_morales/Box\ Sync/InsightNY/Data/Jul2013_2014/SItickets.csv' 
	    INTO TABLE SItable  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
       LINES TERMINATED BY '\n'
       IGNORE 1 LINES;


#INPUTS DATA ON PARKING TICKETS VIOLATIONS AND CODES
DROP TABLE IF EXISTS ViolationTable;
CREATE TABLE ViolationTable (
	ViolationCode INT, 
	Definition TEXT,
	Manh_under96 INT,
	OtherFines INT
);

LOAD DATA LOCAL INFILE '/Users/marco_morales/Box\ Sync/InsightNY/Data/ParkingViolationCodes_clean.csv' 
	INTO TABLE ViolationTable FIELDS TERMINATED BY ',' ENCLOSED BY '"'
	LINES TERMINATED BY '\n'
	IGNORE 1 LINES;