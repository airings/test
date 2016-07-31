'''
Created on Jul 27, 2016

@author: airings
'''
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from TimDemoController import load_data_excel
from flask.templating import render_template
import os

app = Flask(__name__)
app.secret_key = 'random string'
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
  return '.' in filename and \
      filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET'])
def index():
    data = load_data_excel("../file/output_read.xlsx", "Diff")
    metric = load_data_excel("../file/output_read.xlsx", "Metric")
    return render_template('Diff.html', tables = [data.to_html(classes=['dt', 'table', 'table-striped', 'table-bordered']), metric.to_html()], titles = ['na', 'Female surfers', 'Male surfers'])

@app.route('/process', methods=['GET'])
def process():
    data = ''
    metric = ''
    return render_template('Diff.html', tables = [data.to_html(classes=['dt', 'table', 'table-striped', 'table-bordered']), metric.to_html()], titles = ['na', 'Female surfers', 'Male surfers'])


@app.route('/upload',methods=['POST'])
def upload():
      # Get the name of the uploaded files
  uploaded_files = request.files.getlist("file[]")
#   print uploaded_files
  filenames = []
  for file in uploaded_files:
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
      # Make the filename safe, remove unsupported chars
      filename = secure_filename(file.filename)
      # Move the file form the temporal folder to the upload
      # folder we setup
      file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      flash('Finish uploading '+filename)
      # Save the filename into a list, we'll use it later
      filenames.append(filename)
      # Redirect the user to the uploaded_file route, which
      # will basicaly show on the browser the uploaded file
  # Load an html page with a link to each uploaded file
    else:
        flash(file.filename+' is not allowed to upload')
    flash("end")
  return redirect(url_for('index'))



# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)