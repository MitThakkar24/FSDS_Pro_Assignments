from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# Dictionary to store user sessions
user_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    user_id = request.sid
    user_sessions[user_id] = set()
    emit('message', 'Connected to the server.')

@socketio.on('join')
def on_join(data):
    user_id = request.sid
    room = data['room']
    join_room(room)
    user_sessions[user_id].add(room)
    emit('message', f'Joined room: {room}')
    send_notification(room, f'Welcome to {room}!')  # Send welcome notification

@socketio.on('leave')
def on_leave(data):
    user_id = request.sid
    room = data['room']
    if user_id in user_sessions and room in user_sessions[user_id]:
        leave_room(room)
        user_sessions[user_id].remove(room)
        emit('message', f'Left room: {room}')
        emit('notification', f'You left {room} room')
    else:
        emit('message', f'Error: You are not in room {room}')



def send_notification(room, message):
    socketio.emit('notification', message, room=room)

# Simulation of generating notifications
def update_notification():
    while True:
        message = 'New update available!'
        room = 'updates'  # Room name for updates
        send_notification(room, message)
        time.sleep(5)

if __name__ == '__main__':
    # Start the background thread for generating notifications
    update_thread = threading.Thread(target=update_notification)
    update_thread.daemon = True
    update_thread.start()

    socketio.run(app, debug=True)
