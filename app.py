# Importing packages
from flask import Flask
import datetime
import uuid
import json
app = Flask(__name__)

#Api
@app.route('/UUID-timestamp')
def uuidTimestamp():
    time = str(datetime.datetime.now())
    uuidGen = str(uuid.uuid1())
    generateUuid = {
        time: uuidGen
    }
    with open('uuid.json', 'r+') as file:
        data = json.load(file)
        data.update(generateUuid)
        file.seek(0)
        json.dump(data, file)
    with open('uuid.json') as response:
        payload = json.load(response)
    return payload

if __name__ == "__main__":

  app.run(debug=True)