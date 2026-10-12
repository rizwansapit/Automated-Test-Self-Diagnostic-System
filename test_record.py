#importing library
import os
import psycopg
from dotenv import load_dotenv
from datetime import datetime

#electrical test simulation
electrical_test = {
	"test_id": "ELEC-0001",
	"timestamp": datetime.now().isoformat(timespec="seconds"),
	"input_voltage": 12.0,
	"fuse_status": "intact",
	"switch_status": "closed",
	"measured_value": 12.0,
	"nominal_value": 12.0,
	"lower_limit": 11.4,
	"upper_limit": 12.6,
	"unit": "V DC"
}

#simulate electrical output based on component conditions
if (
	electrical_test['fuse_status'] == "intact"
	and electrical_test['switch_status'] == "closed"
):
	electrical_test['measured_value'] = electrical_test['input_voltage']
else:
	electrical_test['measured_value'] = 0.0

#condition for electrical test
if electrical_test["lower_limit"]<= electrical_test["measured_value"] <= electrical_test["upper_limit"]:
		electrical_test["result"] = "PASS"
else:
		electrical_test["result"] = "FAIL"


# Condition for electrical diagnosis
if electrical_test["fuse_status"] == "open":
    electrical_test["diagnostic"] = "OPEN_FUSE"

elif electrical_test["switch_status"] == "open":
    electrical_test["diagnostic"] = "SWITCH_OPEN"

elif electrical_test["input_voltage"] < 11.4:
    electrical_test["diagnostic"] = "INPUT_VOLTAGE_ABNORMAL"

elif electrical_test["input_voltage"] > 12.6:
    electrical_test["diagnostic"] = "INPUT_VOLTAGE_ABNORMAL"

elif electrical_test["measured_value"] < electrical_test["lower_limit"]:
    electrical_test["diagnostic"] = "BELOW_LOWER_LIMIT"

elif electrical_test["measured_value"] > electrical_test["upper_limit"]:
    electrical_test["diagnostic"] = "ABOVE_UPPER_LIMIT"

else:
    electrical_test["diagnostic"] = "NORMAL_OPERATION"


print("\n====== ELECTRICAL TEST REPORT ======")
print(f"Test ID 		:{electrical_test['test_id']}")
print(f"Test Parameter  	:Switched output Voltage")
print(f"Measured value  	:{electrical_test['measured_value']} {electrical_test['unit']}")
print(f"Acceptance      	:{electrical_test['lower_limit']} - {electrical_test['upper_limit']} {electrical_test['unit']}")
print(f"Result          	:{electrical_test['result']}")
print(f"Diagnostic      	:{electrical_test['diagnostic']}")
print("======================================")

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

print("\n=======  MECHANICAL TEST REPORT =======")
print(f"Test ID			:{test_record['test_id']}")
print(f"Test Parameter		:{test_record['test_parameter']}")
print(f"Measured Value		:{test_record['measured_value']} {test_record['unit']}")
print(f"Acceptance		:{test_record['lower_limit']} - {test_record['upper_limit']} {test_record['unit']}")
print(f"Result			:{test_record['result']}")
print(f"Diagnostic		:{test_record['diagnostic']}")
print("==========================================")

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

            # 1. Save mechanical test record
            cur.execute(
                """
                INSERT INTO test_history (
                    test_id, timestamp, test_parameter,
                    measured_value, nominal_value,
                    lower_limit, upper_limit, unit,
                    result, diagnostic
                )
                VALUES (
                    %(test_id)s, %(timestamp)s, %(test_parameter)s,
                    %(measured_value)s, %(nominal_value)s,
                    %(lower_limit)s, %(upper_limit)s, %(unit)s,
                    %(result)s, %(diagnostic)s
                )
                """,
                test_record
            )

            # 2. Save electrical test record
            cur.execute(
                """
                INSERT INTO test_history (
                    test_id, timestamp, test_parameter,
                    measured_value, nominal_value,
                    lower_limit, upper_limit, unit,
                    result, diagnostic
                )
                VALUES (
                    %(test_id)s, %(timestamp)s, %(test_parameter)s,
                    %(measured_value)s, %(nominal_value)s,
                    %(lower_limit)s, %(upper_limit)s, %(unit)s,
                    %(result)s, %(diagnostic)s
                )
                """,
                {
                    **electrical_test,
                    "test_parameter": "Switched Output Voltage"
                }
            )

    print("Mechanical test records saved.")
    print("Electrical test record saved.")

except Exception as error:
    print("Database save failed:", error)