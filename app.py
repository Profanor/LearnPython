#import dependencies
from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

#initialize flask instance
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Change this if using MongoDB Atlas
db = client.tododb  # Create/use database 'tododb'
todos_collection = db.todos  # Create/use collection 'todos'

@app.route('/')
def index():
    todos = list(todos_collection.find())
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        todos_collection.insert_one({'text': todo})
    return redirect(url_for('index'))

@app.route('/delete/<todo_id>')
def delete_todo(todo_id):
    todos_collection.delete_one({'_id': ObjectId(todo_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)