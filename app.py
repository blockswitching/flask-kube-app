from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/docker')
def about_docker():
    return render_template('docker.html')


@app.route('/flask')
def about_flask():
    return render_template('flask_page.html')


@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')


@app.route('/health')
def health():
    return 'All systems operational'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
