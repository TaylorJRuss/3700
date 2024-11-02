from flask import Flask, render_template
from util import connect_to_db, disconnect_from_db, run_and_fetch_sql

app = Flask(__name__)


username='russtay'
password='database'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/api/update_basket_a', methods=['GET'])
def update_basket_a():
    try:
        cursor, connection = connect_to_db(username, password, host, port, database)
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s)", (5, 'Cherry'))
        connection.commit()
        disconnect_from_db(connection, cursor)
        return "Success!"
    except Exception as e:
        return str(e)

@app.route('/api/unique', methods=['GET'])
def unique_fruits():
    try:
        cursor, connection = connect_to_db(username, password, host, port, database)
        unique_a = run_and_fetch_sql(cursor, "SELECT fruit_a FROM basket_a WHERE fruit_a NOT IN (SELECT fruit_b FROM basket_b)")
        unique_b = run_and_fetch_sql(cursor, "SELECT fruit_b FROM basket_b WHERE fruit_b NOT IN (SELECT fruit_a FROM basket_a)")
        disconnect_from_db(connection, cursor)

        unique_a = [item[0] for item in unique_a]
        unique_b = [item[0] for item in unique_b]

        html = "<table border='1'><tr><th>Unique Fruits in Basket A</th><th>Unique Fruits in Basket B</th></tr>"
        for fruit_a, fruit_b in zip(unique_a, unique_b):
            html += f"<tr><td>{fruit_a}</td><td>{fruit_b}</td></tr>"
        html += "</table>"

        return render_template('index.html', sql_table=html, table_title="Unique Fruits")
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
