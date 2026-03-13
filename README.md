# Smart-File-Organizer
A smart and interactive Command Line Interface(CLI) tool written in Python. It helps you automatically sort the messy folders based on customizable rules(file extensions, keywords)

## Features
* **Interactive CLI:** A user-friendly menu that guides you through rule creation, file organization and rule inspection
* **Smart Sorting:** Sort files not only by their extensions(e.g. `.pdf`, `.jpg`) but also by precise keyword matching in the filename (e.g. `homework`, `exam`). These rules are customizable
* **Failsafe Mechanisms:**
  * **Overwrite Warning:** Requires a confirmation before wiping out existing rules.
  * **Safe Exit:** Type 'q' at any promt during rule creation to safely abort the process.
  * **Conflict Resolution:** Automatically appends a counter (e.g. `filename` + `_1`) with the same name already exists in the destination folder. Prevents file to be overwritten
  * **Rule Visualization:** A built-in "Check the rules" operation allows translte raw JSON data in the a human-readable layout.
  * **State Persistence:** All sorting rules are saved locally in a `config.json` file that can be constanly used in the future.

## Getting Started

### Requirement
* Python 3.x installed on your machine
* Built-in python libraries(`os`, `shutil`, `json`)

### Installation
1. Clone the repository or download the source code:
    ```bash
   git clone https://github.com/yourusername/Smart-File-Organizer.git
   cd Smart-File-Organizer
   ```
2. Run the main script in your terminal:
   ```bash
   python smart_organizer.py
   ```
## Usage

Upon running the script, there will be 4 options on the main:

### 1. Create completely new rules or cover the existing rules
Follow the prompts to define your sorting criteria:
* **Format**: The file extension you want to sort(e.g. , `.pdf`, `.docs`, separated by spaces)
* **Keywords**: Specific words the filename contains (e.g., `homework`. Press Enter to skip if no keywords are required)
* **Destination**: The name of the subfolder where mathcing files will be allocated

*(Tip: Type `q` at any input prompt during this process to safely cancel and return to the main menu.)*

### 2. Organize the files with the existing rules
Input the **path** of the directory you want to organize. The script will read your `config.json` and move the matchign files into their designated sufolders.

### 3. Check the rules
Prints all currenly active rules from `config.json`

```text
=== Current Rules ===

Rule: 1
Extensions: .pdf
Keywords: homework
Destination Folder: Graded_Homework

Rule: 2
Extensions: .pdf, .docs
Keywords:
Destination Folder: Other

=====================
```

### 4.Exit
Safely close the application

## Project Structure

```text
Smart-File-Organizer/
├── smart_organizer.py     # Main entry point and interactive CLI menu
├── config.json            # Auto-generated configuration file storing your rules
├── README.md              # Project documentation
└── utils/
    └── rules_apply.py     # Core logic (config creation, smart sorting)
