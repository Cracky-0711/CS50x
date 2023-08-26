# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import hashlib
import os

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'your-secret-key'  # ?
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# モデルの定義
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    salt = db.Column(db.String(200), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='incomplete')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # ランダムなソルトを生成

    # ソルトとパスワードを結合してハッシュ化
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    return salt, hash_obj

def verify_password(saved_salt, saved_hash, input_password):
    hash_obj = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), saved_salt, 100000)
    return hash_obj == saved_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and verify_password(user.salt, user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        error = 'Username or password is incorrect.'
        return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error = 'This username is not available.'
            return render_template('signup.html', error=error)
        salt, hash_obj = hash_password(password)
        new_user = User(username=username, password=hash_obj, salt=salt)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/index')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        deadline = request.form['deadline']
        new_task = Task(title=title, deadline=deadline, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.deadline = request.form['deadline']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
