import psycopg2
from psycopg2 import Error

# this function is based on the tutorial at: https://pynative.com/python-postgresql-tutorial/
def connect_to_db(username='russtay', password='database', host='127.0.0.1', port='5432', database='dvdrental'):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=username, password=password, host=host, port=port, database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        print("connected to the database")

        return cursor, connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def disconnect_from_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
        print("Connection does not work.")


def run_and_fetch_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        record = cursor.fetchall()
        return record
    except (Exception, Error) as error:
        print("Errors while executing the code: ", error)
        return -1
        record = cursor.fetchall()
        return record
    except (Exception, Error) as error:
        print("Errors while executing the code: ", error)
        return -1
