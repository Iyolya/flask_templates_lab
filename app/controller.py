from flask import render_template, request
from app.models.event_class import Event
from app.models.our_events import events
from app import app

# from app.models.event_class import Event

@app.route("/")
def index():
    #return "Hello World!"
    return render_template('index.html', title="Home", events=events)