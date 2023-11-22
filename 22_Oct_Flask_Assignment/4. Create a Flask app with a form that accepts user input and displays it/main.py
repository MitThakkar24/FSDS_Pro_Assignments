from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('submit.html', username=username)
    return 'Something went wrong'

if __name__ == '__main__':
    app.run(debug=True)