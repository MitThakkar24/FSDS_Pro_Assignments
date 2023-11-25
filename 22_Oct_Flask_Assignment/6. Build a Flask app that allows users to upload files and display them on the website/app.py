from flask import Flask, render_template, request, redirect
import os
import json

with open('config.json', 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)

# Define the upload folder and allowed file extensions 
UPLOAD_FOLDER =  r"C:\Users\Asus\OneDrive - GUJARAT POWER ENGINEERING AND RESEARCH INSTITUTE\Learning\GitHub\FSDSP-Assignments\22_Oct_Flask_Assignment\6. Build a Flask app that allows users to upload files and display them on the website\static\uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the file to the upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        filepath = file.filename
        return render_template('upload.html', filename = file.filename) # redirect(url_for('display_file', filename=file.filename))

    return 'Invalid file format! Allowed formats: txt, pdf, png, jpg, jpeg, gif'



if __name__ == '__main__':
    app.run(debug=True)
