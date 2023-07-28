
# SimpleFileCleaner.py

SimpleFileCleaner is a Python script that helps you clean up directories by deleting files and directories based on specified rules. It provides various functions to delete files and directories using regular expressions.

## Requirements
- Python 3 - To install Python 3, please visit the official website: [https://www.python.org/](https://www.python.org/)

## Usage

1. Clone the repository or download the SimpleFileCleaner.py script.

2. Create a config.txt file in the same directory as the SimpleFileCleaner.py script. The config.txt file will contain rules for file and directory cleanup.

3. Configuring the config.txt file:
   - The config file contains instructions for the script to perform cleaning operations.
   - You can specify an optional execution time for the cleaning operations using the format `H:XX:XX`. For example, `H:03:05` will execute the cleaning at 3:05 AM daily.
   - Add files or directories to delete in the config file. To specify a file or directory with a regular expression, write the regex after the path, separated by a colon `:`.

4. Run the SimpleFileCleaner.py script with Python 3:
   ```bash
   python3 SimpleFileCleaner.py
   ```
   The script will read the config.txt file and perform the specified cleanup operations.

## Types of Deletion
The script supports different types of deletion specified by the first letter of each line in the config.txt file:
- `P`: Set the path to the directory to clean
- `D`: Delete all directories that match the regex in the specified path
- `DR`: Delete all directories that match the regex in the specified path and in all subdirectories
- `F`: Delete all files that match the regex in the specified path
- `FR`: Delete all files that match the regex in the specified path and in all subdirectories
- `A`: Delete all files and directories that match the regex in the specified path
- `AR`: Delete all files and directories that match the regex in the specified path and in all subdirectories
- `E`: Delete all empty directories that match the regex in the specified path
- `ER`: Delete all empty directories that match the regex in the specified path and in all subdirectories

## Example config.txt
```
# This is the config file for the SimpleFileCleaner.py script
# If you want to specify an hour when the clean must be executed, use H:XX:XX at the start of the file
# You can add files or directories to delete in this file
# To add a file or directory, just write the path to the file or directory
# To add a file or directory with a regex, write the regex after the path, separated by a ':'
# You specify the type of deletion with the first letter of the line, then ":", then the regex
# The types are:
# P : Set the path to the directory to clean
# D : Delete all directories with the regex in the path
# DR : Delete all directories with the regex in the path and in all subdirectories
# F : Delete all files with the regex in the path
# FR : Delete all files with the regex in the path and in all subdirectories
# A : Delete all files and directories that match the regex in the path
# AR : Delete all files and directories with the regex in the path and in all subdirectories
# E : Delete all empty directories with the regex in the path
# ER : Delete all empty directories with the regex in the path and in all subdirectories

# Example:
# H:03:05
# P:/Users/username/Desktop
# D:myDirectory_*
# P:/Users/username/Documents
# F:myFile_*
# ER:*

# Every day, at 3:05 AM:
# This will delete all directories starting with "myDirectory_" in the Desktop directory
# Then it will delete all files starting with "myFile_" in the Documents directory
# Then it will delete all empty directories in the Documents directory and in all subdirectories
```

## Note
- Lines starting with '#' are considered comments and will be ignored by the script.
- If you encounter any issues or need help, please feel free to contact the author (Noy) or refer to the script's documentation.

## Author
- [Noy](https://github.com/4Noy)

## Version
- 0.1

Please note that this README provides a general overview of the application. For a more detailed understanding of the code and functionalities, refer to the source code and comments within the Python script.

For safe usage, just modify ini.json.