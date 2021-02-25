from flask import Flask, request
from db_connector import *
import signal
import os
app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        try:
            name = request.json.get('user_name')
            add_username(name, user_id)
            return {'status': 'ok', 'user added': name}, 200  # status code
        except:
            return {'status': 'error', 'reason': "id already exists"}, 500  # status code# status code
    elif request.method == 'GET':
        try:
            name = get_user_info(user_id)
            return {'status': 'ok', 'name': name}, 200  # status code
        except:
            return {'status': 'error', 'reason': "No such id"}, 500  # status code# status code
    elif request.method == 'DELETE':
        try:
            delete_user(user_id)
            return {'status': 'ok', 'the following user was deleted': user_id}, 200  # status code
        except:
            return {'status': 'error', 'reason': "No such id"}, 500  # status code# status code
    elif request.method == 'PUT':
        try:
            name = request.json.get('user_name')
            update_user_name(user_id,name)
            return {'status': 'ok', 'user_updated': name}, 200  # status code
        except:
            return {'status': 'error', 'reason': "no such id"}, 500

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped', 200

app.run(host='0.0.0.0', debug=True, port=5000)
