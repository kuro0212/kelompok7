from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data_anggota', methods=['GET', 'POST'])
def dataa():

    return render_template('data_anggota.html')


if __name__ == '__main__':
    app.run(debug=True  port=8000, host='0.0.0.0')
