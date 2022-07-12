from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import Flask
from flask import request
from flask import jsonify
import re
import os
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
import tensorflow_hub as hub

print("new")
#model = hub.load(r"https://tfhub.dev/google/universal-sentence-encoder-large/5")
print("model loaded")

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   req = request.get_json()
   name = req["name"]
   return name


if __name__ == '__main__':
   app.run()

   
   
