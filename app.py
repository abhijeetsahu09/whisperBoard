from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

SUPABASE = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE, SUPABASE_KEY)

@app.route('/', methods=['GET'])
def index():
    result = supabase.table('tasks').select('*').execute()
    tasks = result.data if result.data else []
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    description = request.form['description']
    supabase.table('tasks').insert({'task': task, 'description': description}).execute()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        task = request.form['task']
        description = request.form['description']
        supabase.table('tasks').update({'task': task, 'description': description}).eq('id', task_id).execute()
        return redirect(url_for('index'))
    result = supabase.table('tasks').select('*').eq('id', task_id).execute()
    task = result.data[0] if result.data else None

    result_all = supabase.table('tasks').select('*').execute()
    tasks = result_all.data if result_all.data else []
    return render_template('index.html', tasks=tasks, edit_task=task)


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    supabase.table('tasks').delete().eq('id', task_id).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)