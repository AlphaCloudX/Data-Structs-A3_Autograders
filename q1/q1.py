import csv
import subprocess

msg = """

8888888888                           888    d8b                        8888888888                           888                    
888                                  888    Y8P                        888                                  888                    
888                                  888                               888                                  888                    
8888888    .d88888 888  888  8888b.  888888 888  .d88b.  88888b.       8888888    .d88888 888  888  8888b.  888888 .d88b.  888d888 
888       d88" 888 888  888     "88b 888    888 d88""88b 888 "88b      888       d88" 888 888  888     "88b 888   d88""88b 888P"   
888       888  888 888  888 .d888888 888    888 888  888 888  888      888       888  888 888  888 .d888888 888   888  888 888     
888       Y88b 888 Y88b 888 888  888 Y88b.  888 Y88..88P 888  888      888       Y88b 888 Y88b 888 888  888 Y88b. Y88..88P 888     
8888888888 "Y88888  "Y88888 "Y888888  "Y888 888  "Y88P"  888  888      8888888888 "Y88888  "Y88888 "Y888888  "Y888 "Y88P"  888     
               888                                                                    888                                          
               888                                                                    888                                          
               888                                                                    888                                          

By Michael
"""

print(msg)
programName = input("What is the program name:")

# Initialize counters for passes, fails, and list for failed files
passes = 0
fails = 0
failed_lines = []


def run_a3(option, expression):
    # Open A3.exe with the equation argument
    process = subprocess.Popen(
        ['A3.exe', expression],
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
            recieved = run_a3(option, equation)





            if row[option] in recieved:
                print(f"\033[32mOption: {option}\033[0m")
                print(f"\033[32m[EXPECTED]:{row[option]}\033[0m")
                print(f"\033[32m[RECEIVED]:{parsed(recieved)}\033[0m")
                print(f"\033[32mPASS\033[0m")
                passes += 1

            else:
                fails += 1
                failed_lines.append(equation)
                print(f"\033[31mOption: {option}\033[0m")
                print(f"\033[31m[EXPECTED]:{row[option]}\033[0m")
                print(f"\033[31m[RECEIVED]:{parsed(recieved)}\033[0m")
                print("RAW OUTPUT FOR DEBUGGING:")
                print(recieved)
                print(f"\033[31mFAIL\033[0m")

        print("\n\n")

# At the end, print the summary of passes and fails
print(f"\nSummary: {passes} PASS, {fails} FAIL")

# If there are any failed files, display them
if fails > 0:
    print("\nExpressions that failed:")
    for failed_file in failed_lines:
        print(f"\"{failed_file}\"")
