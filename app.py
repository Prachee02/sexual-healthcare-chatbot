from flask import Flask, render_template, request, jsonify
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from chat import get_response
import torch
import json
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/consult_doctor')
def consult_doctor():
    return render_template('consult_doctor.html')

@app.route('/symptom')
def ask_query():
    return render_template('symptom.html')

@app.route('/blogs')
def read_blogs():
    return render_template('blogs.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
