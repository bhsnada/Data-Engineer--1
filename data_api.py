from flask import Flask, jsonify
import sqlite3
from database import connect, get_sample_data

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the ETL and API application!'


@app.route('/read/first-chunk', methods=['GET'])
def read_chunk():
    try:
        connection = connect()
        data = get_sample_data(connection)
        response = jsonify(data)
        response.status_code = 200
        return response
    except Exception as e:
        error_message = {'error': str(e)}
        response = jsonify(error_message)
        response.status_code = 500
        return response


if __name__ == '__main__':
    app.run(debug=True)
