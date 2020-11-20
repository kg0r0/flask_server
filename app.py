from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def root():
  return render_template("index.html")

@app.route("/info")
def info():
  return request.get_data()

if __name__ == "__main__":
  app.run(port=8888)