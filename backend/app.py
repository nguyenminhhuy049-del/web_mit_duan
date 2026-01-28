from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route('/api/movies')
def get_movies():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cinema_db"
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT title, genre, duration FROM movies")
    data = cursor.fetchall()
    return jsonify(data)
@app.route('/api/showtimes')
def get_showtimes():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cinema_db"
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT show_date, show_time, movie_id
        FROM showtimes
        ORDER BY show_date, show_time
    """)
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
