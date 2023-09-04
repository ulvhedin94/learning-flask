from flask import Flask, request, abort
from flask import render_template
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return 'siema'