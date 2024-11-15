import os
import shutil
import subprocess


def print_deepheap_with_border():
    print("+---------------------------------------------------------+")
    print("| DDDD  EEEEE  EEEEE  PPPP     H   H  EEEEE  AAAAA  PPPP  |")
    print("| D   D E      E      P   P    H   H  E     A     A P   P |")
    print("| D   D EEEE   EEEE   PPPP     HHHHH  EEEE  AAAAAAA PPPP  |")
    print("| D   D E      E      P        H   H  E     A     A P     |")
    print("| DDDD  EEEEE  EEEEE  P        H   H  EEEEE A     A P     |")
    print("+---------------------------------------------------------+")


# Function to remove special characters from a string
def clean_content(content):
    return ''.join(e for e in content if e.isalnum() or e.isspace())


# Call the function to display the ASCII art with borders
print_deepheap_with_border()

programName = input("What is the program name:")

# Set up paths and filenames
input_folder = "inputFiles"
output_folder = "userGenerated"
expected_folder = "expectedFiles"  # Folder where the expected output .dat files are stored
exe_name = programName
exe_path = os.path.join(os.getcwd(), exe_name)  # Assuming exe is in the root directory

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Initialize counters for passes, fails, and list for failed files
passes = 0
fails = 0
failed_files = []

# Step 1: Process each file in the input folder
paths = os.listdir(input_folder)
for original_filename in paths:
    original_path = os.path.join(input_folder, original_filename)

    # Skip if the file is the .exe itself
    if original_filename == exe_name:
        continue

    # Step 2: Copy the file to the root directory and rename it to f.dat
    copied_file_path = os.path.join(os.getcwd(), "f.dat")
    shutil.copy(original_path, copied_file_path)

    # Step 3: Run the .exe with the renamed f.dat
    output_file_path = "output.txt"
    subprocess.run([exe_path], stdout=open(output_file_path, 'w'))

    # Step 4: Move and rename the output file
    new_output_path = os.path.join(output_folder, f"{original_filename.split('.')[0]}.dat")
    shutil.move(output_file_path, new_output_path)

    # Step 5: Clean up by removing the copied f.dat from the root directory
    os.remove(copied_file_path)

    # Step 6: Clean the output file and compare it with the expected result
    with open(new_output_path, 'r') as output_file:
        output_content = output_file.read()
        cleaned_output = clean_content(output_content)

    # Read the expected output from the expectedFiles folder
    expected_filename = f"{original_filename.split('.')[0]}.dat"
    expected_file_path = os.path.join(expected_folder, expected_filename)

    try:
        with open(expected_file_path, 'r') as expected_file:
            expected_content = expected_file.read()
            cleaned_expected = clean_content(expected_content)

        # Step 7: Compare the cleaned output and expected content
        if cleaned_output == cleaned_expected:
            print(f"\033[32mPASS:\033[0m {original_filename}")
            passes += 1  # Increment pass counter
        else:
            print(f"\033[31mFAIL:\033[0m {original_filename}")
            fails += 1  # Increment fail counter
            failed_files.append(original_filename)  # Add to failed files list

    except FileNotFoundError:
        print(
            f"Expected file {expected_filename} not found in {expected_folder}. Skipping comparison. This Should Not Happen!")

# At the end, print the summary of passes and fails
print(f"\nSummary: {passes} PASS, {fails} FAIL")

# If there are any failed files, display them
if fails > 0:
    print("\nFiles that failed:")
    for failed_file in failed_files:
        print(f"- {failed_file}")
