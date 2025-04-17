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
    ensureLogExists()
    with open(logFile, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def saveLog(data):
    with open(logFile, 'w') as f:
        json.dump(data, f, indent=4)