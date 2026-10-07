from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/page2")
def page2():
    return "This page is to let me know the apllication works perfect locally"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)