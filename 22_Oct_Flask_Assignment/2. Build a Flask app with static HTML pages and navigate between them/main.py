from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/navigation')
def NavigationPage():
    return render_template('Navigate.html')

if __name__ == '__main__':
    app.run(debug=True)