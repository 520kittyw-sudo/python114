from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# 設定資料庫路徑 (使用 SQLite)
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'students.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定義資料庫模型 (這裡以學生資料為例)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    major = db.Column(db.String(50), nullable=False)

# 自動建立資料庫檔案
with app.app_context():
    db.create_all()

# --- CRUD 功能路由 ---

# Read: 讀取所有資料並顯示
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Create: 新增資料
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    major = request.form.get('major')
    if name and major:
        new_student = Student(name=name, major=major)
        db.session.add(new_student)
        db.session.commit()
    return redirect(url_for('index'))

# Delete: 刪除資料
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('index'))

# Update: 修改資料 (這裡簡化為編輯頁面)
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    student = Student.query.get(id)
    if student:
        student.name = request.form.get('name')
        student.major = request.form.get('major')
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)