import json

def json_to_csv(json_content):
    data = json.loads(json_content)

    # Use the first row's keys for fieldnames
    fieldnames = data[0].keys()

    csv_data = ','.join(fieldnames) + '\n'
    csv_data += '\n'.join(','.join(str(row[field]) for field in fieldnames) for row in data)
    
    return csv_data