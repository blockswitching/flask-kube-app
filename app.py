from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health():
    return 'All systems operational'

@app.route('/endpoint')
def endpoint():
    return 'This is a endpoint'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    

