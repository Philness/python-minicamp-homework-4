from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/movie", methods = ["POST"])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form["name"]
    year = request.form["year"]
    genre = request.form["genre"]
    freshness = request.form["freshness"]

    try:
        cursor.execute('INSERT INTO movies(name, year, genre, freshness) VALUES (?,?,?,?)', (name, year, genre, freshness))
        connection.commit()
        message = "Data added into the movies database!"

    except:
        connection.rollback()
        message = "Data not added anywhere!"

    finally:
        connection.close()
        return message

@app.route("/movies")
def movies():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    movie_list = cursor.fetchall()
    connection.close()
    return jsonify(movie_list)

app.run(debug=True)
