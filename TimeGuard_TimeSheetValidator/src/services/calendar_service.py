import json
import os

def get_calendar_events():
    with open('src/static/mock_calendar.json', 'r') as f:
        return json.load(f)['events']