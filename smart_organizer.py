import os
import json

from utils.rules_apply import config_creation
from utils.rules_apply import file_organize

def main():

    print("\n===Welcome to the Smart-File-Organizer===")

    while True:
        print("\nPlease choose your operation")
        print("1. Create completely new rules or cover the existing rules for organization")
        print("2. Organize the files with the existing rules")
        print("3. Check the rules")
        print("4. Exit")

        choice = input("\nPlease type in your choice(1/2/3/4): ").strip()

        if choice == '1':

            existing_rules = []
            is_appending = False
            action_status = False

            if os.path.exists("config.json"):
                print("\nThe rules already exist")

                while True:
                    action = input("Do you want to append(a) new rules or overwrite(o) the old rules completely?(a/o, or 'q' to quit): ").strip().lower()
                    if action == 'q':
                        action_status = True
                        break

                    elif action == 'a':
                        is_appending = True
                        with open("config.json", 'r', encoding='utf-8') as read:
                            existing_config = json.load(read)
                            existing_rules = existing_config.get("Rules", [])
                        print("\nNew rules will be appended to the existing rules.")
                        break

                    elif action == 'o':
                        confirm = input("\nThe following action will completely cover your existing rules. Are you sure to continue?(y/n): ").strip()
                        if confirm != 'y':
                            action_status = True
                        break
                    else:
                        print("\nInvalid input. Please type 'a', 'o' or 'q'.")
                
                if action_status:
                    print("\nReturn to the menu.")
                    continue

            print("\nHints:Type q at any time to cancel and return to the menu.\n\nPlease don't name your folder 'q'.")

            sort_rule_list = []
            quit = False

            while True:
                ft_input = input("\nPlease type in the format of the file you want to sort(separated by spaces, e.g., .pdf, .jpg): ").lower().strip()
                # e.g.: /Users/markusliu/Downloads/code_test
                if ft_input == 'q':
                    quit = True
                    break
                file_type = ft_input.split()

                fkey_input = input("\nPlease type in the keywords that might appear in the file name"
                "(such as 'invoice', 'exam') separated by spaces. If none, press enter): ").lower().strip()

                if fkey_input == 'q':
                    quit = True
                    break
                file_keyword = fkey_input.split() 

                destination_directory = input("\nPlease name the folder that the sorted files will be allocated(Only type one): ").strip()

                single_rule = {
                    "Extensions": file_type,
                    "File_Keyword": file_keyword,
                    "Destination": destination_directory
                }
                sort_rule_list.append(single_rule)

                continue_edition = input("\nDo you want to add another rule? (y/n): ").strip()
                if continue_edition == 'q':
                    quit = True
                    break
                elif continue_edition != 'y':
                    break

            if quit:
                print("\nReturn to the menu.")
            else:
                save = input("\nAre you sure to save the edited rules(y/n): ").strip().lower()
                if save == 'y':
                    if is_appending:
                        existing_rules.extend(sort_rule_list)
                        config_rule = {"Rules": existing_rules}
                    else:
                        config_rule = {"Rules": sort_rule_list}

                    config_creation(config_rule)
                    print("\nRules are created and saved to config.json")
                else:
                    print("\nRules are not saved.")
        
        elif choice == '2':
            if not os.path.exists("config.json"):
                print("\nError: No rules found. Please create a rule(Option 1) before organizing files.")
                continue
                
            target_directory = input("\nPlease enter the directory you want to sort(Only one directory): ").strip()
            if os.path.isdir(target_directory):
                with open("config.json") as c:
                     config = json.load(c)
                file_organize(target_directory, config)
                print("\nOrganization complete.")
            else:
                print("\nDirectory not existed. Please try again.")
        
        elif choice == '3':
            if os.path.exists("config.json"):
                with open("config.json", 'r', encoding='utf-8') as read:
                    config = json.load(read)
                print("\n=== Current Rules ===\n")
                for i, rule in enumerate(config.get("Rules",[]),1):
                    ext = ", ".join(rule["Extensions"])
                    keyword = ", ".join(rule["File_Keyword"])
                    dest = rule["Destination"]
                    print(f"Rule: {i}\nExtensions: {ext}\nKeywords: {keyword}\nDestination Folder: {dest}\n")
                print("=====================")
            else:
                print("\nRules do not exist")

        elif choice == '4':
            print("\nThanks for using\n")
            break

        else:
            print("\nInvalid type in, please try again(1/2/3/4)")

if __name__ == "__main__":
    main()






    
