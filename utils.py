import json
from datetime import datetime




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

    for y in entry:
        print (y,':',entry[y])

addNewEntry()
