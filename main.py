from log_handler import ensureLogExists




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

    if "5" in option or "exit" in option.lower():
        exit()



main()


