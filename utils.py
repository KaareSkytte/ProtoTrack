import json
from datetime import datetime
from log_handler import * 

def addNewEntry():
    projectName = input("Enter project name: ")
    reponsiblePerson = input("Who's responsible for the project: ")
    logTitle = input("Enter title for log entry: ")
    logDes = input("Describe the change: ")
    references = input("Enter references: ")
    date = datetime.today().strftime('%d/%m/%Y')

    entry = {
        "Project": "",
        "Responsible": "",
        "Title": "",
        "Description": "",
        "References": "",
        "Date": "",
    }

    entry["Project"] = projectName
    entry["Responsible"] = reponsiblePerson
    entry["Title"] = logTitle
    entry["Description"] = logDes
    entry["References"] = references
    entry["Date"] = date

    logData = loadLog()
    logData.append(entry)
    saveLog(logData)
    
    print("Entry added successfully.")


