from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask App."

if __name__ == '__main__':
    app.run(debug=True)