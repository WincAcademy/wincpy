import json
import os


def get_countries():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data_fp = open(os.path.join(module_path, "countries.json"), "r")
    return json.load(data_fp)["countries"]
