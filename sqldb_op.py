import MySQLdb
import pymysql

DATABASE_HOUSEINFO = {
    'host':'127.0.0.1',
    'database':'houseinfo',
    'user':'root',
    'password':'test',
    'charset':'utf8mb4'
    }
DATABASE_FLIGHTS = {
    'host':'127.0.0.1',
    'database':'flights',
    'user':'root',
    'password':'test',
    'charset':'utf8mb4'
    }

conn = MySQLdb.connect(host = 'localhost',user = 'root',password = 'test',db = 'flights')
   
mycursor  = conn.cursor()

'''
    CREATE TABLE `flights` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`origin` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`destination` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	duration INT(11) NOT NULL,
	PRIMARY KEY (id)
    );
'''
sql_createTb = """CREATE TABLE `flights` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`origin` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`destination` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	duration INT(11) NOT NULL,
	PRIMARY KEY (id)
    );"""

mycursor.execute(sql_createTb)
conn.commit()
 
'''
sql_createTb
CREATE TABLE `passengers` (
`id` INT(11) NOT NULL AUTO_INCREMENT,
`name` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
flights_id INT(11) NOT NULL REFERENCES flights(id),
PRIMARY KEY (id)
)
'''

sql_createTb = """CREATE TABLE `passengers` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
   `name` VARCHAR(80) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
   flight_id INT(11) NOT NULL REFERENCES flights(id), 
   PRIMARY KEY (id))"""

mycursor.execute(sql_createTb)
conn.commit()
conn.close()
   



'''
results = cursor.fetchall()
for row in results:
    print(row)
'''