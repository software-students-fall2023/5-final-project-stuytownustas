from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import pymongo

app = Flask(__name__)


MONGO_URI= "mongodb://mongodb:27017"
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
# task_database = client[os.getenv("MONGODB_DATABASE")]
task_database = client['task_database']
# tasks = task_database[os.getenv("MONGODB_COLLECTION")]
tasks = task_database['tasks']


def insert_task(title, description, priority, status, deadline):
  tasks.insert_one({"title": title, "description": description, "priority": priority, "status": status, "deadline": deadline})

insert_task("Do laundry", "do the laundry", "low", "in progress", "Dec 15")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'GET':
        # Retrieve search query if provided
        search_query = request.args.get('search', '').strip()

        # Query tasks based on the search query
        if search_query:
            task_list = list(tasks.find({'description': {'$regex': search_query, '$options': 'i'}}))
        else:
            task_list = list(tasks.find())

        # Convert ObjectId to string for JSON serialization
        for task in task_list:
            task['_id'] = str(task['_id'])

        return render_template('tasks.html', tasks=task_list, search_query=search_query)

    elif request.method == 'POST':
        data = request.form.get('description', '')

        if data:
            task = {'description': data}
            task_id = tasks.insert_one(task).inserted_id
            return redirect(url_for('manage_tasks'))
        else:
            return jsonify({'error': 'Task description cannot be empty'}), 400
        
@app.route('/tasks/delete/<string:task_id>', methods=['POST'])
def delete_task(task_id):
    task_id = ObjectId(task_id)
    tasks.delete_one({'_id': task_id})
    return redirect(url_for('manage_tasks'))

@app.route('/tasks/delete-page')
def delete_tasks_page():
    task_list = list(tasks.find())

    # Convert ObjectId to string for JSON serialization
    for task in task_list:
        task['_id'] = str(task['_id'])

    return render_template('delete_tasks.html', tasks=task_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)


# for x in tasks.find():
  # print(x)