from flask import Flask, render_template
import os


app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('./index.html')

@app.route("/<username>/<int:post_id>")
def hello_world2(username=None, post_id= None):
    return render_template('./index.html', name = username, user_id = post_id)


@app.route("/blog")
def blog():
    return render_template('./about_me.html')

