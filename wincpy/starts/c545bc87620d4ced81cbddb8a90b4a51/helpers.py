import json

def get_countries():
    return json.load(open('countries.json', 'r'))['countries']
