from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/Users/Drew/Documents/School/Berkeley/year1/calhacks'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import pdf2txt
import os
import sys

file_name = ''

@app.route('/parse/')
def parse():

    open('output.txt', 'w').close()
    os.system('pdf2txt.py -o output.txt ' + file_name)
    output = open('output.txt', 'r+')
    words = {}
    lst = []
    for line in output:
        try:
            pg = int(line)
            words[pg] = lst
            lst = []
        except:
            lst += line.split()
    print(words)

    os.system("python2.7 extractor.py {0}".format(file_name))
    return 'Success'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            global file_name
            file_name = filename
            print(filename)
            print(file_name)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('.parse'))
    return render_template('up.html')

@app.route('/uploads/<filename>/')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
  app.run(debug=True)