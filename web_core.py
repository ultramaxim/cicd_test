#!flask/bin/python
from flask import Flask
from flask import request
import datetime
import re
import pytz

app = Flask(__name__)


# curl -X POST -H "Content-Type: application/json; charset=UTF-8" http://10.66.8.21:5000/api_get_time
@app.route("/api_get_time", methods=["POST"])
def api_get_time():
    return "Current date and time UTC: "+str(datetime.datetime.now(pytz.utc))+"\n"


# curl -X POST -H "Content-Type: application/json; charset=UTF-8" --data '{"a":"5","b":"10","operation":"+"}' http://10.66.8.21:5000/api_get_calculate
@app.route("/api_get_calculate", methods=["POST"])
def api_get_calculate():
    if request.is_json:
        a = request.json.get("a")
        b = request.json.get("b")
        operation = request.json.get("operation")
        check_input = check_input_data(a, b, operation)
        if check_input == "check done":
            return self_calculator(a, b, operation) + "\n"
        else:
            return check_input
    else:
        return "No input JSON data"


def self_calculator(a, b, operation):
    if operation == '+':
        return str(int(a) + int(b));
    if operation == '-':
        return str(int(a) - int(b));
    if operation == '*':
        return str(int(a) * int(b));
    if operation == '/':
        if (b == '0'):
            return "Infinity"
        else:
            return str(int(a) / int(b));


# curl -X POST -H "Content-Type: application/json; charset=UTF-8" http://10.66.8.21:5000/api_get_help
@app.route("/api_get_help", methods=["POST"])
def api_get_help():
    curl_command = "use this curl command to check my project:\n" \
                   "curl -X POST -H \"Content-Type: application\/json; charset=UTF-8\" (optional) --data '{JSON DATA}' http://x.x.x.x:port/method\n"
    use_help_get_time = "api_get_time - use POST request without params to get current time\n"
    use_help_get_calculate = "api_get_calculate - use follow JSON format {\"a\": your_data ,\"b\": your_data,\"operation\": operation above digits} " \
                             "[example: \'{\"a\":\"5\",\"b\":\"10\",\"operation\":\"+\"}\']\n"
    use_help_get_help = "api_get_help - use POST request without params to get HELP\n"
    return curl_command + "\nAPI:\n" + use_help_get_time + use_help_get_calculate + use_help_get_help


def check_input_data(a, b, operation):
    pattern = r"\A\d+\Z"
    if re.match(pattern, a):
        if re.match(pattern, b):
            pattern_operation = r"\A[\+\-\*\\/]{1,1}\Z"
            if re.match(pattern_operation, operation):
                return "check done"
            else:
                return "invalid input for param 'operation'"
        else:
            return "invalid input for param 'b'"
    else:
        return "invalid input for param 'a'"


app.run(host='0.0.0.0', port=5000)
#
