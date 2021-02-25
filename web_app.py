from flask import Flask
from db_connector import *
import signal
import os
app = Flask(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>')
def user(user_id):
    try:
        name = get_user_info(user_id)
        return "<H1 id='user'>" + name + "</H1>", 200
    except:
        return "<H1 id='error'>""no such user: " + user_id + "</H1>", 500

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped', 200

app.run(host='127.0.0.1', debug=True, port=5001)
