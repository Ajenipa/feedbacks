from flask import Flask,redirect,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import sqlalchemy
app=Flask(__name__)
Bootstrap(app)
@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)