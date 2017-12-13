import os

FILENAME = 'request_counts.txt'
REQUESTS = ['GET', 'POST', 'DELETE', 'PUT']

def read_file():
    """Returns a dictionary with the requests stored in the txt file."""
    count = {'GET': 0,
         'POST': 0,
         'DELETE': 0,
         'PUT': 0}
    with open(os.path.join(os.path.dirname(__file__), FILENAME), 'r') as textfile:
        for i, line in enumerate(textfile.readlines()):
            count[REQUESTS[i]] += int(line.split(" ")[1])
    return count

def write_file(count):
    """Gets the dictionary of all the requests as a parameter. Writes it into the textfile\
    as expected. Returns None"""
    with open(os.path.join(os.path.dirname(__file__), FILENAME), 'w') as textfile:
        for req in REQUESTS:
            output = req + ': ' + str(count[req]) + '\n'
            textfile.write(output)
