from flask import Flask, jsonify,request
from flask_cors import CORS



# configuration
DEBUG = True

TASKS = [
    {
        'task': '777x Design build',
        'status': 'requirment',
        'deadline':'10 days remaining'
    },
    {
        'task': '737MAX AOA design',
        'status': 'test',
        'deadline':'50 days remaining'
    },
    {
        'task': 'NMA part configuration',
        'status': 'requirment',
        'deadline':'5 days remaining'
    },
    {
        'task': '787 system test',
        'status': 'design',
        'deadline':'20 days remaining'
    },
    {
        'task': 'poc work',
        'status': 'review',
        'deadline':'2 days remaining'
    },
    
]
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TASKS.append({
            'task': post_data.get('task'),
            'status': post_data.get('status'),
            'deadline': post_data.get('deadline')
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()