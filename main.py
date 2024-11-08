from flask import Flask
from views.home import *
from configuration import configure_all

app=Flask(__name__)

configure_all(app)

if(__name__=="__main__"):
    app.run(debug=True)