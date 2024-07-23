from flask import Flask, render_template, request
from downloader import downloader

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        link = request.form.get('url')
        download_format = request.form.getlist('format')
        downloader(link,download_format)
    return render_template('index.html')

@app.route('/download')
def download():
    return render_template('download.html')

if __name__ == "__main__":
    app.run()