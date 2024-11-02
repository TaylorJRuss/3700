def connect_to_db(username='russtay', password='database', host='127.0.0.1', port='5432', database='dvdrental'):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=username, password=password, host=host, port=port, database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
@@ -23,7 +19,7 @@ def connect_to_db(username='russtay', password='database', host='127.0.0.1', por

def disconnect_from_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
@@ -38,8 +34,3 @@ def run_and_fetch_sql(cursor, sql_string=""):
    except (Exception, Error) as error:
        print("Errors while executing the code: ", error)
        return -1
