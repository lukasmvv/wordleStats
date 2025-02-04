# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import os

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files = str(list(os.listdir(current_directory+"\\data"))) + "\n"
    subfolders = [f.name for f in os.scandir(current_directory) if f.is_dir()]
    return files

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()