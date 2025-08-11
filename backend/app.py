from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# For simplicity, we'll use an in-memory list as our "database"
tasks = [
    {'id': 1, 'title': 'Learn Flask', 'done': True},
    {'id': 2, 'title': 'Build a Todo App', 'done': False},
]
next_id = 3

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': next_id,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    done = request.json.get('done')
    if done is None:
        return jsonify({'error': 'Done status is required'}), 400

    task['done'] = bool(done)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5001)
