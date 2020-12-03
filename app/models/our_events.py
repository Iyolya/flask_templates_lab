from app.models.event_class import *


event_1 = Event("02", "big event")
event_2 = Event("03", "small event")
events = [event_1, event_2]


def list_events(event_list):
    return events

print(events)