from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
#import pdf2txt
import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
UPLOAD_FOLDER = '/Users/Drew/Documents/School/Berkeley/year1/calhacks/CalHacksBowles2016/viewer'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



file_name = ''

@app.route('/parse/')
def parse():

    open('output.txt', 'w').close()
    #os.system('pdf2txt.py -o output.txt ' + file_name)
    output = open('output.txt', 'r+')
    words = {}
    lst = []
    for line in output:
        try:
            pg = int(line)
            words[pg] = lst
            lst = []

            #print("python2.7 split.py {0} {1}".format(file_name, pg))
            #os.system("python2.7 split.py {0} {1}".format(file_name, pg))
            #print("python2.7 extractor.py tmp/placeholder.pdf {1}".format(pg))
            #os.system("python2.7 extractor.py tmp/placeholder.pdf {1}".format(pg))

        except:
            #print("whaaaaat")
            lst += line.split()
    # EXTRACT IMAGES

    #step1 - splitpdf
    inputpdf = PdfFileReader(open(file_name, "rb"))
    os.system('rm -r slide*')
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        os.system('mkdir slide'+str(i+1))
        with open("slide"+str(i+1)+"/page"+str(i+1)+".pdf", "wb") as outputStream:
            output.write(outputStream)
    for i in range(1,inputpdf.numPages+1):
        os.system('pdfimages -j slide'+str(i)+'/page'+str(i)+'.pdf slide'+str(i)+'/foo') # extract image
        os.system('pdftotext slide'+str(i)+'/page'+str(i)+'.pdf') # extract text
        #os.system('rm slide'+str(i)+'/page'+str(i)+'.pdf')
    print(words)

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