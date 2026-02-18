# prompt-tracker.py
import datetime  # This is a built-in library for dates and times

def main():
    print("--- Welcome to your AI Prompt Tracker! ---")
    
    while True:
        print("\nMenu:")
        print("1. Add Prompt")
        print("2. View Prompts")
        print("3. Search Prompts")
        print("4. Delete Prompt") # New Option!
        print("5. Quit")
        
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            text = input("Enter the prompt text: ")
            cat = input("Category (learning/creating/evaluating/other): ").lower()
            note = input("Short note on when to use it: ")
            
            # --- GET THE DATE ---
            # .strftime formatting gives us "Year-Month-Day Hour:Minute"
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # We add 'now' to our saved string
            with open("my-prompts.txt", "a") as f:
                f.write(f"{now}|{cat}|{text}|{note}\n")
            print(f"Prompt saved on {now}!")

        elif choice == '2':
            print("\n--- Your Saved Prompts ---")
            try:
                with open("my-prompts.txt", "r") as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 4: # Changed to 4 because of the date
                            p_date, category, p_text, p_note = parts
                            print(f"({p_date}) [{category.upper()}]")
                            print(f"Prompt: {p_text}")
                            print(f"Note: {p_note}\n")
            except FileNotFoundError:
                print("No prompts saved yet!")

        elif choice == '3':
            query = input("Enter a keyword to search for: ").lower()
            found = False
            try:
                with open("my-prompts.txt", "r") as f:
                    for line in f:
                        if query in line.lower():
                            p_date, category, p_text, p_note = line.strip().split('|')
                            print(f"MATCH: [{category}] {p_text} (Saved: {p_date})")
                            found = True
                if not found:
                    print("No matches found.")
            except FileNotFoundError:
                print("No file found to search.")

        elif choice == '4':
            # --- DELETE PROMPT ---
            try:
                # 1. Read everything into a list so we can count them
                with open("my-prompts.txt", "r") as f:
                    lines = f.readlines()
                
                if not lines:
                    print("Nothing to delete.")
                    continue

                # 2. Show the list with numbers
                print("\nWhich prompt would you like to delete?")
                for i, line in enumerate(lines):
                    # We use i + 1 because humans like counting from 1, not 0
                    print(f"{i + 1}. {line.strip()}")
                
                del_choice = int(input("\nEnter the number to delete: "))
                
                # 3. Write everything BACK, except the one we don't want
                # We subtract 1 to get back to Python's 0-based counting
                with open("my-prompts.txt", "w") as f:
                    for i, line in enumerate(lines):
                        if i != (del_choice - 1):
                            f.write(line)
                
                print("Prompt deleted successfully!")

            except (FileNotFoundError, ValueError, IndexError):
                print("Oops! Invalid selection or file is empty.")

        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()