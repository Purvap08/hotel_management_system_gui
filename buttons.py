import mysql.connector
db=mysql.connector.connect(
		host="Localhost",
		user="root",
		password="",
		database="hotel_management",
		#port=""
)
cur=db.cursor()
print(db)