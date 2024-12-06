from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('game'))


@app.route('/game')
def game():
    return render_template('2048.html')


@app.errorhandler(404)
def no_url_found(error):
    return 'Page not found', 404


@app.route('/add/<int:num1>/<int:num2>')
def add_in_url(num1, num2):
    return str(num1 + num2)


@app.route('/check/<any(green, blue, red):color>')
def take_url_args(color):
    return color


@app.route('/query', methods=['GET'])
def take_query_str():
    name = request.args.get('name')
    return f"Hello {name if name else 'Anonymous'}"


@app.route('/data', methods=['POST'])
def take_form_data():
    data = request.form
    name = data.get('name')
    return f"Hello {name if name else 'Anonymous'}"


@app.route('/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file:
        # check file size
        if len(file.read()) > 1024 * 1024 * 2:
            return 'File size exceeds limit of 2MB'
        return 'File uploaded successfully'
    else:
        return 'No file uploaded'


if __name__ == '__main__':
    app.run(debug=True)
