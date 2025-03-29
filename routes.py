from flask import render_template, redirect, url_for, request
from app import app
from app.utils import save_api_keys

@app.route('/')
def home():
    api_keys = load_api_keys()
    if api_keys:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    reddit_api_key = request.form['reddit_api_key']
    openai_api_key = request.form['openai_api_key']
    
    api_keys = {
        'reddit': reddit_api_key,
        'openai': openai_api_key
    }
    
    save_api_keys(api_keys)
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    api_keys = load_api_keys()
    return render_template('dashboard.html', api_keys=api_keys)
