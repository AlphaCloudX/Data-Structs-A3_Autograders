# How to Run

### Step 1: Downloading the Script

- **GUI Interface**:  
  If you're using a GUI interface, simply press the "Code" button and download the ZIP file.  
  Then, extract the contents to your desired location.

- **Terminal Interface**:  
  If you're using a terminal, download the program by running the following command:

  ```bash
  wget https://github.com/AlphaCloudX/Data-Structs-A3_Autograders/archive/refs/heads/main.zip
  ```
  After downloading, extract the ZIP file with:
  ```bash
  unzip main.zip
  ```

    Then navigate to where your MakeFile is and comile your project to get the a3q2 executable:
  ```bash
  cd /where/your/make/file/is
  ```

  Then compile
  ```bash
  make
  ```

  Then to keep track of where the executable is located run:
  ```bash
  pwd
  ```
  
  Back up to where the unzipped autograder is, might require doing `c..` a few times, then navigate to the folder for the grader you want to use.
  
  Question 1 Autograder:
  ```bash
  cd Data-Structs-A3_Autograders-main/q1
  ```

  Question 2 Autograder:
  ```bash
  cd Data-Structs-A3_Autograders-main/q2
  ```

  Then copy your a3q1 or a3q2 file inside the current directory here.
  ```bash
  cp /path/to/source/a3q2 .
  ```


### Step 2: Provide the Executable File

Before running the script, ensure that the `.exe` or `.out` file is copied into the `q1` or `q2` folder(depending on the autograder being used). Can be done via terminal or gui.

Once the file is in the folder, when prompted, enter the filename of the executable (e.g., `yourfile.exe` or `yourfile.out`).

### Step 2: Run the Script

To execute the program, run the following python command:

Do note that q1.py will only work when inside the q1 folder as it's for question 1.

The same way, q2.py will only work when inside the q2 folder as it's for question 2.

```bash
python q1.py
python q2.py
```

or

```bash
python3 q1.py
python3 q2.py
```

### Additional Information

Question 1:
- 360 Test Cases
- Super Sensitive To The Main and Format So Debugging Print Statements Are Enabled

Question 2:
- This program is designed to process **1000 test cases**.
- Fairly Positive This Is Fully Correct
