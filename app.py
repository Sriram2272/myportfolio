import os
from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import re

# Create Flask app
app = Flask(__name__)
app.config['SRIRAM_PORTFOLIO_DB_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')  # Use environment variable
app.config['SRIRAM_PORTFOLIO_TRACK_MODIFICATIONS'] = False

# Map custom keys to standard SQLAlchemy keys
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SRIRAM_PORTFOLIO_DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config['SRIRAM_PORTFOLIO_TRACK_MODIFICATIONS']

# Initialize DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Contact Model
class Contact(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    reason = db.Column(db.String(200), nullable=False)  # Removed unique=True
    date = db.Column(db.String(12), nullable=True)

    def __init__(self, name: str, phone: str, email: str, reason: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.reason = reason
        self.date = datetime.now().strftime('%Y-%m-%d')

    def __repr__(self) -> str:
        return f'<Contact {self.name}>'

# GitHub Repo Fetcher (update to your GitHub username)
def get_projects():
    api_url = 'https://api.github.com/users/sreeram-dama/repos'
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 403:  # Rate limit exceeded
            print("GitHub API rate limit exceeded.")
            return []
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching GitHub repos: {e}")
        return []

# Routes
@app.route('/')
def main_page():
    return render_template('index.html', title='Dama Sri Ram - Homepage')

@app.route('/home')
def home():
    return render_template('base.html', title='Base')

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    contact_info_included = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        reason = request.form.get('reason', '').strip()

        contact_info_included = False
        if 10 <= len(phone) <= 13 and re.fullmatch(r'^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$', phone):
            try:
                entry = Contact(name, phone, email, reason)
                db.session.add(entry)
                db.session.commit()
                contact_info_included = True
            except Exception as e:
                print(f"Database error: {e}")

    return render_template('contact.html', title='Contact Page', contact_status=contact_info_included)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', title="Projects", cards=get_projects())

# Make `now` available in templates
@app.context_processor
def inject_now():
    return {'now': datetime.now}

# Error Handlers
@app.errorhandler(404)
def err_404(error):
    return render_template('error.html', message='404 - Page Not Found'), 404

@app.errorhandler(Exception)
def handle_exception(error):
    print(f"Unhandled Exception: {error}")  # Log the error for debugging
    return render_template('error.html', message="Something went wrong."), 500
