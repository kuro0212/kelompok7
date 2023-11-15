from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data_anggota', methods=['GET', 'POST'])
def dataa():

    return render_template('data_anggota.html')


if __name__ == '__main__':
    app.run(debug=True)
