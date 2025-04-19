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

def viewAllEntries():
    log = loadLog()    
    
    for i in range(len(log)):
        print("Project      : ", log[i]["Project"])
        print("Responsible  : ", log[i]["Responsible"])
        print("Title        : ", log[i]["Title"])
        print("Description  : ", log[i]["Description"])
        print("References   : ", log[i]["References"])
        print("Date         : ", log[i]["Date"], "\n")


def getFilter():
    filterType = input("Enter you choice: ")
    return filterType

def filterEntries():
    print("Choose filter type:")
    print("1. Project")
    print("2. Responsible person")
    print("3. Date")

    while True:    
        filterType = getFilter()

        if "1" in filterType or "project" in filterType.lower():
            filterKey = "Project"
            break

        elif "2" in filterType or "person" in filterType.lower():
            filterKey = "Responsible"
            break

        elif "3" in filterType or "date" in filterType.lower():
            filterKey = "Date"
            break
        
        else: 
            print("Invalid Choice\n")
            
    filterValue = input("Enter a filter value: ")
    log = loadLog()

    filteredEntries = []

    for i in range(len(log)):
        if filterValue.lower() in log[i][filterKey].lower():
            filteredEntries.append(log[i])
        
    if len(filteredEntries) != 0:
        for i in range(len(filteredEntries)):
            print("Project      : ", filteredEntries[i]["Project"])
            print("Responsible  : ", filteredEntries[i]["Responsible"])
            print("Title        : ", filteredEntries[i]["Title"])
            print("Description  : ", filteredEntries[i]["Description"])
            print("References   : ", filteredEntries[i]["References"])
            print("Date         : ", filteredEntries[i]["Date"], "\n")
    else: 
        print("No Entries Found...")


def exportData():
    exportType = input("Choose export format (1. for plain text, 2 for markdown): ")

    if exportType == "1":
        fileExtension = ".txt"
        format = "text"

    elif exportType == "2":
        fileExtension = ".md"
        format = "markdown"

    else: 
        print("Invalid choice")
        return

    name = input("Enter a file name: ")
    log = loadLog()
    fileName = name +  fileExtension

    def formatEntry(entry, format):
        if format == "text":
            return (
                f"Project: {entry['Project']}\n"
                f"Responsible: {entry['Responsible']}\n"
                f"Title: {entry['Title']}\n"
                f"Description: {entry['Description']}\n"
                f"References: {entry['References']}\n"
                f"Date: {entry['Date']}\n"
                + "-" * 30 + "\n"
            )
        elif format == "markdown":
            return (
                f"### Project: {entry['Project']}\n"
                f"- **Responsible**: {entry['Responsible']}\n"
                f"- **Title**: {entry['Title']}\n"
                f"- **Description**: {entry['Description']}\n"
                f"- **References**: {entry['References']}\n"
                f"- **Date**: {entry['Date']}\n"
                + "---\n"
            )

    with open (fileName, 'w+') as f:
        for entry in log:
            f.write(formatEntry(entry, format))

    print(f"Log exported successfully as {fileName}")


