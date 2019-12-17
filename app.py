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
    cmd = "python model/src/predict.py"
    os.system(cmd)

    f = open("result.txt", "r")
    try: 
        predictedUser = f.readlines()[0].strip()
    except: 
        predictedUser = '0'
        
    f.close()
        
    if os.path.exists("result.txt"):
        os.remove("result.txt")

    if predictedUser == '1':
        return render_template('result1.html')
    elif predictedUser == '2':
        return render_template('result2.html')
    elif predictedUser == '3':
        return render_template('result3.html')
    else:
        return render_template('noresult.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
