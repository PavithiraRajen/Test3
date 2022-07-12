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


#model = hub.load(r"https://tfhub.dev/google/universal-sentence-encoder-large/5")


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()

   
