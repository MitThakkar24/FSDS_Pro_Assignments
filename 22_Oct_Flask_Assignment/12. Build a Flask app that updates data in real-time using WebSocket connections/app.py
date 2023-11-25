from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

data = {'value': 0}

def update_data():
    while True:
        time.sleep(1)
        data['value'] += 1
        socketio.emit('update', data)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('update', data)

if __name__ == '__main__':
    update_thread = threading.Thread(target=update_data)
    update_thread.daemon = True
    update_thread.start()
    socketio.run(app, debug=True)
