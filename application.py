from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World Azure Pipelines Build! This will go to both pipelines but I'll still keep the deploy part. Seriously, screw you azure. That's it for the evening"
