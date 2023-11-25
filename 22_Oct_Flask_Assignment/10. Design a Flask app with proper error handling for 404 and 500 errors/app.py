from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route that doesn't exist to trigger 404 error
@app.route('/')
def index():
    # Simulate a 404 error by not returning anything
    return render_template('index.html')

# Custom error handler for 404 Not Found and 500 Internal Server Error
@app.errorhandler(404)
@app.errorhandler(500)

def not_found_error(error):
    return render_template('Error.html',title=error.name, message=error.description), error.code


if __name__ == '__main__':
    app.run(debug=True)
