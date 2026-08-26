from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files.getlist("image"))
    files = request.files.getlist("image")
    print(str(files[0]))
    if (str(files[0]) != "<FileStorage: '' ('application/octet-stream')>"):
        for file in files:
            file.save("/home/srogue/epaper/friends/newImages/" + file.filename)
        return 'File uploaded successfully!'
    else:
        return 'No files were selected'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
