from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

# Simulated user data (Replace this with a database or actual user data)




@app.route('/')
def index():
    return 'Welcome! <a href="/login">Login</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_data = {
    'TMR': {'name': 'TMR', 'email': 'TMR@example.com'},
    'Mit': {'name': 'Mit', 'email': 'Mit@example.com'}
    }

    if request.method == 'POST':
        username = request.form['username']
        # Simulated password check (Replace this with proper authentication)
        if username in user_data:
            user = user_data[username]
            session['username'] = username
            session['user'] = user  # Storing the entire user data in session (for demonstration)
            return redirect(url_for('user_data'))
        else:
            return "Invalid username"
    return render_template('login.html')


@app.route('/user_data')
def user_data():
    username = session.get('username')
    user = session.get('user')
    if username and user:
        return f"User: {user['name']}, Email: {user['email']} <br><a href='/logout'>Logout</a>"
    return "Please login first"


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
