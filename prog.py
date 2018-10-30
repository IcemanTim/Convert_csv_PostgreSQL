
import time
import logging
import csv 
import psycopg2

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'LogFile.log')

try:
	logging.info("Recording db parametres")
	print("Write your database name : ")
	db_name = str(input())
	print("Write your user name : ")
	user_name = str(input())
	print("Write your host : ")
	host = str(input())
	print("Write your password : ")
	password = str(input())
	logging.info("Recording succeeded")

	conn_string="dbname='"+ db_name + "' user='" + user_name + "' host='" + host + "' password='" + password + "'"
	
	logging.info("Connecting to database\n->%s" % (conn_string))
	conn = psycopg2.connect(conn_string)

	logging.info("Connection succeeded")
	cur = conn.cursor()

	try:
		logging.info("Deleting DB")
		cur.execute("""DROP TABLE police_info;""")
		conn.commit()
		logging.info("DB was deleted successfully")
	except:
		logging.error("Error in deleting table")

	try:
		logging.info("Creating DB")
		cur.execute("""CREATE TABLE police_info (
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
										Common_Location VARCHAR );
				""")
		conn.commit()
		logging.info("DB was successfully created")
	except:
		logging.error("Error in creating table")
except:
	logging.error("No connection to db")

logging.info("Program started")

start_time = time.time()
rec_num = 0

logging.info("Putting records in DB : ")
with open("./police-department-calls-for-service.csv", 'r') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	line = []
	for line in reader:
		logging.info("Record %s" %(rec_num))
		logging.info(line)
		rec_num += 1
		logging.info("Insert record with num %s" %(rec_num))
		cur.execute("INSERT INTO police_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", line);
		logging.info("Insert successfull")

logging.info("end of work, closing all")
conn.commit()
cur.close()
conn.close()

logging.info("\n")
logging.info("Loading time : %s seconds\n" % (time.time() - start_time))
logging.info("In total,  to the database were uploaded %s records \n" % (rec_num))

logging.info("Done!")


