from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# Chatroom page
@app.route('/')
def chat():
    return render_template('chat.html')

# Event triggered when a message is received from the client
@socketio.on('message')
def handle_message(msg):
    print('Message:', msg)
    emit('message', msg, broadcast=True)  # Broadcast the message to all connected clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
