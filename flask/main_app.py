import os
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'media/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'xlsx', 'docx'}  # 'gif'

app = Flask(__name__)
app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(
    str(app.config['BASE_DIR']), UPLOAD_FOLDER)

app.secret_key = b'[x[]_5#y2L"F434645gfdddsddfgz\n\xec]/'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def form():
    return render_template('/form.html', **{'title': 'Load file'})


@app.route('/upload/', methods=['POST', ])
def upload():
    # check if the post request has the file part
    if 'file_field' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('form'))

    file = request.files['file_field']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('Please, select a file from your PC!', 'error')
        return redirect(url_for('form'))

    if not allowed_file(file.filename):
        flash('Not allowed file extension! Try again.', 'error')
        return redirect(url_for('form'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(app.config['UPLOAD_FOLDER'] + filename)

        flash(f'New file "{filename}" was uploaded.', 'success')
        return redirect(url_for('uploaded'))
        # return redirect(url_for('processed_file', **{'filename': filename}))


@app.route('/processed/<filename>/')
def processed_file(filename):
    return render_template('/processed.html', **{
        'title': 'This file was uploaded and precessed:',
        'filename': filename
    })


@app.route('/download/<filename>/')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/uploaded/')
def uploaded():
    file_list = []

    for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for filename in files:
            file_list.append(filename)
    if len(file_list):
        return render_template('/uploaded.html', **{
            'title': 'Uploaded files',
            'file_list': file_list
        })
    else:
        flash('Not have uploaded files.', 'warning')
        return redirect(url_for('form'))
