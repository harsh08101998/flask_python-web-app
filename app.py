from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Set up the database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="192.168.64.3",      # Change this to your MySQL host (use "localhost" for local DB)
        user="admin",           # Replace with your MySQL username
        password="admin123",  # Replace with your MySQL password
        database="student_db"   # Replace with your database name
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student')  # Change this to your table name
    students = cursor.fetchall()
    conn.close()
    print(students)
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        student_name = request.form['name']
        student_age = request.form['age']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO student (name, age) VALUES (%s, %s)', (student_name, student_age))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

