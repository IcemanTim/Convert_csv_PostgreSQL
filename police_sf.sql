CREATE TABLE police_info (
	Crime_Id BIGINT NOT NULL PRIMARY KEY,
	Original_Crime_Type_Name VARCHAR,
	Report_Date TIMESTAMP,
	Call_Date VARCHAR,
	Offense_Date TIMESTAMP,
	Call_Time TIME,
	Call_Date_Time TIMESTAMP,
	Disposition VARCHAR,
	Address VARCHAR,
	City VARCHAR,
	State VARCHAR,
	Agency_Id SMALLINT,
	Address_Type VARCHAR,
	Common_Location VARCHAR
);
