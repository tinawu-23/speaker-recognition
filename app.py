import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pydub import AudioSegment

ALLOWED_EXTENSIONS = {'wav'} 

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
            if filename == 'key.wav':
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                audio = AudioSegment.from_wav("./static/files/key.wav")
                print(audio)
                length = audio.duration_seconds
                print(length)
                half = (length//2) * 1000
                wav1 = audio[:half]
                wav1.export('./static/files/key1.wav', format="wav")
                wav2 = audio[half:]
                wav2.export('./static/files/key2.wav', format="wav")
            else:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('upload_file', filename=filename))


@app.route('/process')
def run_model():
    os.system("python model/src/predict.py")
    os.system("python model/src2/pre_process_waveforms.py")
    os.system("python model/src2/predict.py")
    os.system("python model/combined_predict.py")


    f = open("result.txt", "r")
    user = {'1': 'first', '2': 'second', '3': 'third'}

    try:
        predictedUser = f.readlines()[0].strip()
    except:
        predictedUser = ''
    f.close()
            
    if os.path.exists("result.txt"):
        os.remove("result.txt")
    
    allprediction = [user[key] for key in predictedUser.split()]
    display = ''

    plural = False
    if len(allprediction) > 1:
        plural = True
        display += ', '.join(allprediction)
    elif allprediction:
        display += allprediction[0]
    else:
        display = ''
    
    if plural:
        display += " ones are"
    elif not plural and predictedUser != '':
        display += " one is"

    return render_template('result.html', name=display)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
