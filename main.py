from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'
db = SQLAlchemy(app)

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    language = db.Column(db.String(50))

@app.route('/')
def homepage():
    issues = Issue.query.all()
    return render_template('homepage.html', issues=issues)

@app.route('/signup')
def signup():
    issues = Issue.query.all()
    return render_template('signup.html', issues=issues)

@app.route('/login')
def login():
    issues = Issue.query.all()
    return render_template('login.html', issues=issues)

@app.route('/forgot')
def forgot():
    issues = Issue.query.all()
    return render_template('forgot.html', issues=issues)

@app.route('/add_issue', methods=['GET', 'POST'])
def add_issue():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        language = request.form['language']

        new_issue = Issue(title=title, description=description, language=language)
        db.session.add(new_issue)
        db.session.commit()
        return redirect('/')
    return render_template('add_issue.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

