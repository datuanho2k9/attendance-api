from flask import Flask, request
from flask_cors import CORS
import json
import os
from markupsafe import escape

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def mainroute():
    return "Main route"


@app.route('/attend', methods=['POST'])
def attend():
    data = request.json
    path = f'./Database/Classes/{data["class-id"]}.json'
    exist = os.path.exists(path)
    message = {'status': 400, 'message': 'Error is occurred, maybe because the body is not a JSON data, or without '
                                         'header Content-Type:application/json', 'data': None}
    if not exist:
        with open(path, "w") as file:
            file.write(f'["{data["student-id"]}"]')
            message["message"] = f'Attended {data["student-id"]} in {data["class-id"]}'
            message['status'] = 200
    else:
        dataParsed = []
        with open(path, "r") as file:
            dataParsed = json.load(file)
            message = {'status': 300,
                       'message': f'Student {data["student-id"]} is already attended in {data["class-id"]}'
                , 'data': None}
        if data["student-id"] not in dataParsed:
            with open(path, "w") as file:
                dataParsed.append(data["student-id"])
                json.dump(dataParsed, file, indent=4)
                message = {'status': 200,
                           'message': f'Student {data["student-id"]} is added as attended in {data["class-id"]}',
                           'data': None}
    return message


@app.route('/attendance/<id>', methods=['GET'])
def attendance(id):
    path = f'./Database/Classes/{escape(id)}.json'
    exist = os.path.exists(path)
    message = {'status': 400, 'message': 'Class doesn\'t exist', 'data': None}
    if exist:
        with open(path, "r") as file:
            message["status"] = 200
            message['message'] = f"Success fetching data for class {id}"
            message["data"] = json.load(file)
    return message


app.run(debug=True)
