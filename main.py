from flask import Flask, render_template, request, redirect, url_for, session, flash
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

SUPABASE = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE, SUPABASE_KEY)

# Admin login route
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            auth_resp = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if auth_resp.user:
                session['admin'] = True
                return redirect(url_for('home'))
            else:
                flash('Login failed. Check credentials.', 'danger')
        except Exception as e:
            flash('Login failed. Wrong password or user does not exist.', 'danger')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    flash('Logged out.', 'info')
    return redirect(url_for('home'))

# Decorator for admin-only routes
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin'):
            flash('Admin login required.', 'warning')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        rating = int(request.form['rating'])
        comment = request.form['comment']
        supabase.table('feedback').insert({
            'name': name,
            'rating': rating,
            'comment': comment,
        }).execute()
        return redirect(url_for('home'))
    return render_template('feedback.html')

@app.route('/admin/feedback')
@admin_required
def admin_feedback():
    result = supabase.table('feedback').select('*').order('created_at', desc=True).limit(20).execute()
    feedbacks = result.data if result.data else []
    return render_template('admin_feedback.html', feedbacks=feedbacks)

@app.route('/suggest', methods=['GET', 'POST'])
def suggest():
    if request.method == 'POST':
        content = request.form['content']
        supabase.table('suggestions').insert({
            'content': content,
        }).execute()
        return redirect(url_for('home'))
    return render_template('suggestions.html')

@app.route('/admin/suggestions')
@admin_required
def admin_suggestions():
    result = supabase.table('suggestions').select('*').order('created_at', desc=True).limit(20).execute()
    suggestions = result.data if result.data else []
    return render_template('admin_suggestions.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)