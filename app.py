import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'} ##TODO: change this to wav file eventually

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = './static/files'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))


@app.route('/process')
def run_model():
    print("here")
    cmd = "python model/src/predict.py"
    os.system(cmd)
    f = open("result.txt", "r")
    predictedUser = f.readlines()[0].strip()
    return "Predicted User " + str(predictedUser)


if __name__ == "__main__":
    app.run(debug=True, port=5000)