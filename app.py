# import main Flask class and request object
from flask import Flask, request, render_template

app = Flask(__name__)  # create the Flask app

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/upload/file')
def formexample():
    print('hello')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
