from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Connect to the database
def connect_db():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row  # Allows row access by column name
    return conn

# Create the table if it doesn't exist
def create_table():
    conn = connect_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS batch_E (
            roll_no INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()  # Call it when app starts

# Home page with form
@app.route('/')
def home():
    return render_template('student_form.html')

# Form submit and show all students
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll_no = request.form['roll_no']

    conn = connect_db()
    conn.execute('INSERT INTO batch_E (roll_no, name) VALUES (?, ?)', (roll_no, name))
    conn.commit()
    students = conn.execute('SELECT * FROM batch_E').fetchall()
    conn.close()

    return render_template('student_list.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
