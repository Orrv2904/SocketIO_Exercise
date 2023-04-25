from flask import Flask, render_template
from flask_socketio import emit, join_room, leave_room, SocketIO
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on("message") 
def message(data):
  print(data)
  emit("message", data["message"],  broadcast=True)