import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


try: 
	with psycopg.connect(
		dbname=os.getenv("DB_NAME"),
		user=os.getenv("DB_USER"),
		password=os.getenv("DB_PASSWORD"),
		host=os.getenv("DB_HOST"),
		port=os.getenv("DB_PORT")
	) as conn:
		print("PostgreSQL connection succesful!")

except Exception as error:
	print("Connection failed:", error)