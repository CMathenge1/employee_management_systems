from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Welcome to my app."

@app.route("/help")
def okay():
    return render_template("Please check our products.")

@app.route("/bootstrap")
def boot():
    return render_template("mystrap.html")


app.run()