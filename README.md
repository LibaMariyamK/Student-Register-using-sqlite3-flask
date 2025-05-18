# 📝 Student Register - Flask App

A simple web application using **Flask** and **SQLite3** to register students and display the list.

---

## 💡 Features

- Add student details (Name and Roll No.)
- Save data to SQLite database
- View all registered students

---

## ⚙️ Tech Stack

- **Python** 🐍  
- **Flask** 🌐 (Web framework)  
- **SQLite3** 🗃️ (Database)  
- **HTML** 📝 (Jinja Templates)


---

## 📂 Project Structure

```

├── app.py                   # Main Flask app
├── students.db              # SQLite database (auto-created)
└── templates/
├── student\_form.html    # Form to add student
└── student\_list.html    # Display registered students

````

---

## 🧠 Code Summary

### `app.py`

- `connect_db()` → connects to the database
- `create_table()` → creates the `batch_E` table if not exists
- `'/'` route → shows form to add student
- `'/add'` route → inserts new student and displays all students

### `student_form.html`

- Simple form to input Name and Roll No.
- Submits data using POST method to `/add`

### `student_list.html`

- Loops through student data and displays in a table

---



## 📦 Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/student-register.git
cd student-register
````

### 2. Install Flask:

```bash
pip install flask
```

### 3. Run the application:

```bash
python app.py
```

### 4. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🙌 Acknowledgments

This project was created as a learning exercise for understanding Flask and databases.

---
