import sys

def print_menu():
    """Prints the menu of available scripts."""
    
    print("Select a script to run:")
    for i, script in enumerate(scripts):
        print(f"{i + 1}: {script}")

# List of scripts that the user can choose from
scripts = [
    "saveallimages.py",
    "scrapehtml.py",
    "getpagetopdf.py",
    "quit",
]

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
            print(f"Running {script}...")
            exec(open(script).read())
        else:
            raise ValueError
    except ValueError:
        print("Invalid selection.")
