from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__,template_folder='../frontend')
# CORS(app)


@app.route("/")
def Home_page():
    return render_template("index.html")


@app.route("/contactPage")
def contact_page():
    return render_template("contactPage.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

app.run(debug=True)