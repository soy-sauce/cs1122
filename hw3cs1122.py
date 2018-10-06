from flask import Flask
import pymysql.cursors
from pprint import pprint


app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='chalbroker.cs1122.engineering.nyu.edu',
                             user='student',
                             password='student',
                             db='cs1122',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    # get all tables
    with connection.cursor() as cursor:
        query = 'SHOW TABLES'
        cursor.execute(query)
        tables = cursor.fetchall()
        for table in tables:
            print(table)

    # go into students table
    with connection.cursor() as cursor:
        query = "SELECT flag FROM students WHERE net_id = 'cz1529'"
        cursor.execute(query)
        data = cursor.fetchall()
        pprint(data)


finally:
    connection.close()

@app.route('/')
def index():
    return ddata

if __name__ == "__main__":
    app.run(debug=True)
