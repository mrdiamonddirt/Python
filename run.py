import sys
import os

def print_menu():
    """Prints the menu of available scripts."""
    
    print("Select a script to run:")
    for i, script in enumerate(scripts):
        print(f"{i + 1}: {script}")

# Check if the scripts folder exists
if not os.path.exists("scripts"):
    print("Error: the 'scripts' folder does not exist.")
    sys.exit()

# Populate the list of scripts dynamically based on the contents of the 'scripts' folder
scripts = [f for f in os.listdir("scripts") if f.endswith(".py")]

# Add the option to quit to the list of scripts
scripts.append("quit")

while True:
    # Print the menu of available scripts
    print_menu()

    # Get the user's selection
    selection = input("> ")

    # Try to run the selected script
    try:
        index = int(selection) - 1
        if index == len(scripts) - 1:
            # Quit the program
            break
        elif index >= 0 and index < len(scripts) - 1:
            script = scripts[index]
            script_path = f"scripts/{script}"
            # Check if the script file exists
            if not os.path.exists(script_path):
                print(f"Error: {script} does not exist in the 'scripts' folder.")
                continue
            print(f"Running {script}...")
            exec(open(script_path).read())
        else:
            raise ValueError
    except ValueError:
        print("Invalid selection.")
