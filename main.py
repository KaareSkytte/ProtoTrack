from log_handler import ensureLogExists
from utils import *



def main():
    ensureLogExists()
    print("""
    *********************
    welcome to ProtoTrack
    Choose an Option
    *********************
    """)
    
    option = input("""
    1. Add new entry
    2. View all entries
    3. Filter entries
    4. Export log
    5. Exit
    """)    


    if "1" in option or "add" in option.lower():
        addNewEntry()

    if "2" in option or "view" in option.lower():
        viewAllEntries()

    if "3" in option or "filter" in option.lower():
        filterEntries()

    if "4" in option or "export" in option.lower():
        exportData()

    if "5" in option or "exit" in option.lower():
        exit()


main()


