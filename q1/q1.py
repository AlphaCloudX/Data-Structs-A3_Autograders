import csv
import subprocess
import os

msg = """
d88888b  .d88b.  db    db  .d8b.  d888888b d888888b  .d88b.  d8b   db      d88888b  .d88b.  db    db  .d8b.  d888888b  .d88b.  d8888b. 
88'     .8P  Y8. 88    88 d8' `8b `~~88~~'   `88'   .8P  Y8. 888o  88      88'     .8P  Y8. 88    88 d8' `8b `~~88~~' .8P  Y8. 88  `8D 
88ooooo 88    88 88    88 88ooo88    88       88    88    88 88V8o 88      88ooooo 88    88 88    88 88ooo88    88    88    88 88oobY' 
88~~~~~ 88    88 88    88 88~~~88    88       88    88    88 88 V8o88      88~~~~~ 88    88 88    88 88~~~88    88    88    88 88`8b   
88.     `8P  d8' 88b  d88 88   88    88      .88.   `8b  d8' 88  V888      88.     `8P  d8' 88b  d88 88   88    88    `8b  d8' 88 `88. 
Y88888P  `Y88'Y8 ~Y8888P' YP   YP    YP    Y888888P  `Y88P'  VP   V8P      Y88888P  `Y88'Y8 ~Y8888P' YP   YP    YP     `Y88P'  88   YD 

By Michael
"""

print(msg)
programName = input("What is the program name:")

exe_path = os.path.join(os.getcwd(), programName)

# Initialize counters for passes, fails, and list for failed files
passes = 0
fails = 0
failed_lines = []


def run_a3(option, expression):
    # Open A3.exe with the equation argument
    process = subprocess.Popen(
        [exe_path, expression],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Send the option as input followed by Enter
    input_commands = f"{option}\n5\n"  # Assuming 5 is to Exit after the operation

    # Pass the commands to stdin and capture the output
    stdout, stderr = process.communicate(input=input_commands)

    return stdout


def parsed(stdout):
    # Split the output at the first colon ':'
    split_output = stdout.split(':')

    # If the split is successful and there's content after the colon
    if len(split_output) > 1:
        if option == 4:
            cleaned = split_output[3].split("Menu")[0]
        else:
            cleaned = split_output[2].split("Menu")[0]  # Get everything after the first colon
        return cleaned.strip()

    # If no colon is found, return the original output (or handle as needed)
    return stdout.strip()


# Open the CSV file
with open('data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Read and process the rest of the rows
    for row in reader:
        equation = row[0]

        print(f"Processing expression: {equation}")

        for option in [1, 2, 3, 4]:
            received = run_a3(option, equation)

            if row[option] in received:
                print(f"\033[32mOption: {option}\033[0m")
                print(f"\033[32m[EXPECTED]:{row[option]}\033[0m")
                print(f"\033[32m[RECEIVED]:{parsed(received)}\033[0m")
                print(f"\033[32mPASS\033[0m")
                passes += 1

            else:
                fails += 1
                failed_lines.append(equation)
                print(f"\033[31mOption: {option}\033[0m")
                print(f"\033[31m[EXPECTED]:{row[option]}\033[0m")
                print(f"\033[31m[RECEIVED]:{parsed(received)}\033[0m")
                print("RAW OUTPUT FOR DEBUGGING:")
                print(received)
                print(f"\033[31mFAIL\033[0m")

        print("\n\n")

# At the end, print the summary of passes and fails
print(f"\nSummary: {passes} PASS, {fails} FAIL")

# If there are any failed files, display them
if fails > 0:
    print("\nExpressions that failed:")
    for failed_file in failed_lines:
        print(f"\"{failed_file}\"")
