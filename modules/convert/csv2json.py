import csv
import json

def csv_to_json(csv_content):
    csv_reader = csv.DictReader(csv_content.splitlines())
    return json.dumps(list(csv_reader))