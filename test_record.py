#importing library
import os
import psycopg
from dotenv import load_dotenv
from datetime import datetime

#dictionary apa yang di uji
test_record = {
		"test_id": "TST-0001",
		"timestamp": datetime.now().isoformat(timespec="seconds"),
		"test_parameter": "Plate Thickness",
		"measured_value" : 3.1,
		"nominal_value" : 3.0,
		"lower_limit": 2.8,
		"upper_limit": 3.2,
		"unit": "mm",
		"result": "",
		"diagnostic":""
}

#result condition
if test_record["lower_limit"]<=test_record["measured_value"] <= test_record["upper_limit"]:
		test_record["result"] = "PASS"
else:
		test_record["result"] = "FAIL"

#diagnostic condition
if test_record["measured_value"] < test_record["lower_limit"]:
		test_record["diagnostic"] = "BELOW_LOWER_LIMIT"
elif test_record["measured_value"] > test_record["upper_limit"]:
		test_record["diagnostic"] = "ABOVE_UPPER_LIMIT"
else:
		test_record["diagnostic"] = "WITHIN_SPECIFICATION"

print(test_record)

#save test record to database
load_dotenv()
try:
	with psycopg.connect(
		dbname=os.getenv("DB_NAME"),
		user=os.getenv("DB_USER"),
		password=os.getenv("DB_PASSWORD"),
		host=os.getenv("DB_HOST"),
		port=os.getenv("DB_PORT")
	) as conn:
		with conn.cursor() as cur:
			cur.execute(
			"""
			INSERT INTO test_history(
				test_id,timestamp,test_parameter,measured_value,
				nominal_value,lower_limit,upper_limit,unit,result,
				diagnostic
			)
			VALUES(
				%(test_id)s, %(timestamp)s, %(test_parameter)s,
				%(measured_value)s, %(nominal_value)s, 
				%(lower_limit)s, %(upper_limit)s, %(unit)s,
				%(result)s, %(diagnostic)s
			)
			""",
			test_record
		)
	print("Test record saved to PostgreSQL.")

except Exception as error:
	print("Database save failed:", error )