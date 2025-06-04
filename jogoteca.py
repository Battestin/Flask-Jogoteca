from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# Instancia Flask
app = Flask(__name__)

app.config.from_pyfile('config.py')

# Inicializa a extensão SQLAlchemy
db = SQLAlchemy(app)

# Protege de requisições maliciosas
csrf = CSRFProtect(app)

# Ajusta a criptografia das senhas
bcrypt = Bcrypt(app)

from views_games import *
from views_users import *

# Roda o Flask
if __name__ == '__main__':
    app.run(debug=True)