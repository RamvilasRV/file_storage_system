from flask import render_template, url_for, request, send_from_directory, redirect, make_response
from fts import app
import os
import datetime

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("landing.html")

@app.route("/upload_file", methods=['POST', 'GET'])
def upload_file():
    if 'files' not in request.files:
        return "No file part"

    file_list = request.files.getlist('files')
    if len(file_list) == 0:
        return "No selected file"

    if (file_list):
        for file in file_list:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            with open("fts/log.txt", "a") as file:
                log_time = str(datetime.datetime.now())
                log_content= f"Uploaded file '{filename}'"
                log = log_time+" - "+log_content+"\n"
                file.write(log)
        res="Files saved"
    else:
        res="No files found"

    files_present = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("file_display.html", files_present=files_present)

@app.route('/display_files', methods=['GET', 'POST'])
def display_files():
    files_present = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("file_display.html",  files_present=files_present)

@app.route('/display_files_cmd', methods=['GET', 'POST'])
def display_files_cmd():
    files_present = os.listdir(app.config['UPLOAD_FOLDER'])
    response_text = "\n".join(files_present)
    return response_text


@app.route('/download/<filename>', methods=["GET", "POST"])
def download_file(filename):
    with open("fts/log.txt", "a") as file:
        log_time = str(datetime.datetime.now())
        log_content= f"Downloaded file '{filename}'"
        log = log_time+" - "+log_content+"\n"
        file.write(log)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=["POST", "GET"])
def delete_file(filename):
    # return render_template("test.html", filename=filename)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    files_present = os.listdir(app.config['UPLOAD_FOLDER'])
    with open("fts/log.txt", "a") as file:
        log_time = str(datetime.datetime.now())
        log_content= f"Deleted file '{filename}'"
        log = log_time+" - "+log_content+"\n"
        file.write(log)
    files_present = os.listdir(app.config['UPLOAD_FOLDER'])
    return redirect(url_for("display_files"))

















































##
