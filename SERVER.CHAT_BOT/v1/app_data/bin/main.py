#!/usr/bin/python3
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
import sys
import time
from datetime import datetime
from flask import Flask, redirect, url_for, request
import toml, json
import aiml

SERVER_ID = '3f76818f507fe7eb6422bd0703c64c88'
serverType = "CHAT_BOT"
base_config_filePath = "/usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.config/.config"
exception_status = None
try:
    base_config_filePath = sys.argv[1]
except:
    pass

with open(base_config_filePath, 'r') as f:
    BASE_CONFIG_FILE_DATA = toml.loads(f.read())

try:
    with open(BASE_CONFIG_FILE_DATA["config_filePath"]["SYSTEM"], 'r') as f:
        SYSTEM_CONFIG_DATA = toml.loads(f.read())

    with open(BASE_CONFIG_FILE_DATA["config_filePath"]["CHATBOT"], 'r') as f:
        AI_CONFIG_DATA = toml.loads(f.read())
except Exception as e:
    exception_status = e
#with open("HOME_CONTROLLER_COMMANDS.json", 'r') as f:
#    HOME_CONTROLLER_COMMANDS = json.loads(f.read())

CURRENT_CONTROLLER_COMMAND = None
CURRENT_CONTROLLER_RESPONSE = None

NAME = AI_CONFIG_DATA["AI_CORE"]["NAME"]
GENDER = AI_CONFIG_DATA["AI_CORE"]["GENDER"]
BRAIN_LOAD_COMMAND = AI_CONFIG_DATA["AI_CORE"]["BRAIN_LOAD_COMMAND"]
BRAIN_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["BRAIN_FILEPATH"]
BRAIN_BUILD_XML_FILEPATH = AI_CONFIG_DATA["AI_CORE"]["BRAIN_BUILD_XML_FILEPATH"]

# CURRENT_CONTROLLER_FETCHED_RESPONSE = ''

AIML_K = aiml.Kernel()

if os.path.exists(BRAIN_FILEPATH):
    AIML_K.loadBrain(BRAIN_FILEPATH)
    print("LOADED AI BRAIN: " + BRAIN_FILEPATH)

else:
    print("BUILDING AIML BRAIN FROM BRAIN MAP")
    AIML_K.bootstrap(learnFiles=BRAIN_BUILD_XML_FILEPATH, commands=BRAIN_LOAD_COMMAND)
    AIML_K.saveBrain(BRAIN_FILEPATH)
    print("CREATED AI BRAIN: " + BRAIN_FILEPATH)


#command = ''
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return {"server":serverType, "id":SERVER_ID, "timeStamp":time.time(), "exceptionStatus":exception_status}

# USER CONTROLLER ENDPOINTS #
@app.route('/chat_bot/<request>')
#def ai(data):
#    if (home_controller(data)):
#        response = "GETTING RESPONSE FROM THE ROOT HOME CONTROLLER"
#        controller_response = "WAIT"
#    else:
#        response = AIML_K.respond(data)
#        controller_response = None
#    return {
#    "RESPONSE": response,
#    "CONTROLLER_RESPONSE": controller_response
#    }

def chat_bot(request):
    global exception_status
    data={"success":0, 'timeStamp':time.time()}
    try:
        if exception_status:
            data.update({"reason":exception_status})
        else:
            data.update({"response":AIML_K.respond(request)})
    except Exception as e:
        data.update({"reason":e})
    return data


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host=SYSTEM_CONFIG_DATA["SERVICE_INFO"]["HOST"], port=SYSTEM_CONFIG_DATA["SERVICE_INFO"]["PORT"], debug=SYSTEM_CONFIG_DATA["SERVICE_INFO"]["DEBUG_MODE"])
