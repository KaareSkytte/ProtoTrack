# ProtoTrack

**ProtoTrack** is a simple command-line logging tool for tracking changes and updates in design or development projects. It allows users to log entries, filter them by project, person, or date, and export logs in plain text or markdown format.

## Features

- Add log entries with details like project name, responsible person, description, references, and date.
- Filter entries by:
  - Project
  - Responsible person
  - Date
- Export logs to:
  - `.txt` (plain text)
  - `.md` (markdown)

---

## Usage

1. Run the script:
   in bash
   python3 main.py

2. Choose an action:
    Add new log entry
    View all entries
    Filter entries
    Export log


3. Follow the prompts: You'll be guided step-by-step via command line input.


File Structure: 
ProtoTrack/
├── main.py            # Mainlogic
├── utils.py           # Different utilites for functions
├── log_handler.py     # Handles loading and saving log data
├── Logs               
    └── log.json       # Log file (auto-created)
└── README.md          # This file


## Example Entry:

{
  "Project": "Ergo Chair",
  "Responsible": "Kaare",
  "Title": "Adjusted Backrest",
  "Description": "Changed the angle by 5 degrees after user testing",
  "References": "Test Session 03",
  "Date": "17/04/2025"
}
