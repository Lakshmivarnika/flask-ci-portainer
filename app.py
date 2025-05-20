from flask import Flask # type: ignore # Import Flask module
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask + GitHub Actions + Portainer!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
