import json
import os
import shutil

def config_creation(rule: list):
    """
    Create a json file and load rule into it

    Args:
    rule: List. A set of rule that will be written into the file

    """

    filename = "config.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(rule, f, indent=4, ensure_ascii=False)

#***

#
def file_organize(root_path: str, config: dict):
    """
    Organzie the folder with corresponding sorting rule
    
    Args:
    root_path: String. The path of the directory located in the computer
    config: Dictionary. The rules to sort all files in the directory into the corresponding destination directory 
    
    """

    extension_rule_match = {}
    # For all other extensions that don't appear in the config
    general_rule = []

    # Create a dictionary for all extensions appear in the config
    for rule in config["Rules"]:
        if rule["Extensions"]:
            for ext in rule["Extensions"]:
                if ext not in extension_rule_match:
                    extension_rule_match[ext] = []            
                extension_rule_match[ext].append(rule)
        else:
            general_rule.append(rule)
    
    for current_dir, _, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(current_dir, file)

            file_name_l = file.lower()
            ext = os.path.splitext(file_name_l)[-1]

            # Extract the valid rules for the extension
            valid_rule = extension_rule_match.get(ext, []) + general_rule
            valid_rule.sort(key=lambda x: len(x["File_Keyword"]), reverse = True)

            for rule in valid_rule:
                match = True
                for keyword in rule["File_Keyword"]:
                    if keyword not in file_name_l:
                        match = False
                        break
            
                if match:
                    dest_dir = os.path.join(root_path, rule["Destination"])
                    os.makedirs(dest_dir, exist_ok=True)
                    dest_path = os.path.join(dest_dir, file)

                    # To avoid duplicate files with the same name
                    name, _ = os.path.splitext(file_name_l)
                    count = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(dest_dir, f"{name}_{count}{ext}")
                
                    if os.path.abspath(full_path) != os.path.abspath(dest_path):
                        shutil.move(full_path, dest_path)

                    break

