from flask import jsonify, render_template, send_from_directory
from app import app

@app.errorhandler(404)
def no_page_exists(_):
    return render_template('404.html'), 404

@app.errorhandler(500)
def no_page_there(_):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def assets(path):
    return send_from_directory('static',path)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    return jsonify({"hello" : "there we go"})

@app.route('/info')
def info():
    return jsonify({"message" : 123432})


app.secret_key = ''

if __name__ == '__main__':
    app.run(debug=True)
