import os
import json

""" This is a helper function that we provide. Don't delete it! """


def get_countries():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data_fp = open(os.path.join(module_path, "countries.json"), "r")
    return json.load(data_fp)["countries"]
