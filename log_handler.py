import os
import json

logDir = "logs"
logFile = os.path.join(logDir, "log.json")

def ensureLogExists():
    # Checks os path to folder. if false, creates folder
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    
    # Checks for log file. if false, creates file with empty list
    if not os.path.isfile(logFile):
        with open(logFile, 'w+') as f:
            json.dump([], f)


def loadLog():
    with open(logFile, 'r') as f:
        return json.load(f)


def saveLog(data):
    with open(logFile, 'w') as f:
        json.dump(data, f, ident=4)