# Flask-Game-Library

A simple CRUD-based web application to manage a collection of games, built with Flask, MySQL, and WTForms.  
This project was developed during Alura’s **“Getting Started with Flask”** course.

> 🧱 Core functionalities (routing, templates, database integration) were built from scratch as part of the learning experience.

---

## ⚙️ Features

- 🔐 User login/logout with password encryption (Flask-Bcrypt)
- 📋 Add, edit, delete and list games
- 🖼️ Upload cover images for games
- 🧾 Form validation with WTForms
- 💬 Flash messages for user feedback
- 📁 Template inheritance via Jinja2

---

## 🚀 How to Run

1. Create a virtual environment and activate it  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create the database using `prepara_banco.py`  
   (Make sure MySQL is running and credentials are configured in `config.py`)

4. Run the app:  
   ```bash
   python jogoteca.py
   ```

5. Access the application at:
   ```
   http://localhost:5000/
   ```

---

## 🗃️ Folder Structure

```
📦 root
 ┣ 📜 jogoteca.py
 ┣ 📜 config.py
 ┣ 📜 models.py
 ┣ 📜 views_games.py
 ┣ 📜 views_users.py
 ┣ 📜 helpers.py
 ┣ 📜 prepara_banco.py
 ┣ 📁 templates/
 ┃ ┣ 📄 template.html
 ┃ ┣ 📄 lista.html
 ┃ ┣ 📄 editar.html
 ┃ ┣ 📄 novo.html
 ┃ ┗ 📄 login.html
 ┣ 📁 static/
 ┃ ┣ 📄 app.css
 ┃ ┣ 📄 bootstrap.css
 ┃ ┗ 📄 app.js
 ┃ ┗ 📄 jquery.js
 ┗ 📁 uploads/
 ┃ ┗ 📄 capa_padrao.jpg
```

---

## 📦 Requirements

- Python 3.x  
- MySQL Server  
- Flask  
- Flask-SQLAlchemy  
- Flask-Bcrypt  
- Flask-WTF  
- WTForms

All dependencies are listed in `requirements.txt`.

---

## 📄 License

MIT — feel free to use, learn, and improve upon it.
