# rando.py
# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
# Calling Flask function in flask package
# __name__ : built in var in Python
app = fl.Flask(__name__)

# Add root route.
@app.route('/')
def home():
  #return "Hello world."
  return app.send_static_file('index.html')

# tell Flask to make this fn available at /uniform
# dynamic response
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add root route.
# tell Flask to make this fn available at /normal
# dynamic response
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}