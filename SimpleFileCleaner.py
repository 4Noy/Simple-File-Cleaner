#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Noy."
__version__ = "0.1"

"""
NEEDS :
Python 3 - to install : go on the website https://www.python.org/
"""

import os, re, datetime, time, shutil
from datetime import datetime, timedelta

path = os.getcwd()
##############################################################################################################
# FUNCTIONS

def SetPath(_, p):
    """
    Set the path to the directory to clean
    :param p: path to the directory
    :return: None
    """
    global path
    path = p
    if not os.path.exists(path):
        print("Error in the config file : Unkown Path : " + path)
        exit()
    return None

def DelDirectory(path, regexExpression):
    """
    Delete all directories that match the regex in the path
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for file in os.listdir(path):
        if regex.match(file) and os.path.isdir(os.path.join(path, file)):
            shutil.rmtree(os.path.join(path, file))
            print("Deleted Directory : " + os.path.join(path, file))
    return None
def DelDirectoryRecursively(path, regexExpression):
    """
    Delete all Directories that match the regex in the path and in all subdirectories
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for root, dirs, files in os.walk(path):
        for file in dirs:
            if regex.match(file) and os.path.isdir(os.path.join(root, file)):
                shutil.rmtree(os.path.join(root, file))
                print("Deleted Directory : " + os.path.join(root, file))
    return None

def DelFiles(path, regexExpression):
    """
    Delete all files that match the regex in the path
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for file in os.listdir(path):
        if regex.match(file) and os.path.isfile(os.path.join(path, file)):
            os.remove(os.path.join(path, file))
            print("Deleted File : " + os.path.join(path, file))
    return None

def DelFilesRecursively(path, regexExpression):
    """
    Delete all files that match the regex in the path and in all subdirectories
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for root, dirs, files in os.walk(path):
        for file in files:
            if regex.match(file) and os.path.isfile(os.path.join(root, file)):
                os.remove(os.path.join(root, file))
                print("Deleted File : " + os.path.join(root, file))
    return None

def DelAll(path, regexExpression):
    """
    Delete all files and directories that match the regex in the path
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for file in os.listdir(path):
        if regex.match(file) and os.path.isfile(os.path.join(path, file)):
            os.remove(os.path.join(path, file))
            print("Deleted File : " + os.path.join(path, file))
        elif regex.match(file) and os.path.isdir(os.path.join(path, file)):
            shutil.rmtree(os.path.join(path, file))
            print("Deleted Directory : " + os.path.join(path, file))
    return None

def DelAllRecursively(path, regexExpression):
    """
    Delete all files and directories that match the regex in the path and in all subdirectories
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for root, dirs, files in os.walk(path):
        for file in dirs:
            if regex.match(file) and os.path.isdir(os.path.join(root, file)):
                shutil.rmtree(os.path.join(root, file))
                print("Deleted Directory : " + os.path.join(root, file))
        for file in files:
            if regex.match(file) and os.path.isfile(os.path.join(root, file)):
                os.remove(os.path.join(root, file))
                print("Deleted File : " + os.path.join(root, file))
    return None

def DelEmptyDirectories(path, regexExpression):
    """
    Delete all empty directories with the extension in the path
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)) and len(os.listdir(os.path.join(path, file))) == 0 and regex.match(file):
            os.rmdir(os.path.join(path, file))
            print("Deleted Directory : " + os.path.join(path, file))
    return None

def DelEmptyDirectoriesRecursively(path, regexExpression):
    """
    Delete all empty directories with the extension in the path and in all subdirectories
    :param path: path to the directory
    :param extension: extension of the files to delete
    :return: None
    """
    regex = re.compile(regexExpression)
    for root, dirs, files in os.walk(path):
        for file in dirs:
            if os.path.isdir(os.path.join(root, file)) and len(os.listdir(os.path.join(root, file))) == 0 and regex.match(file):
                os.rmdir(os.path.join(root, file))
                print("Deleted Directory : " + os.path.join(root, file))
    return None

def DelSimple(path, dir):
    """
    Delete the given file or directory
    :param path: path to the directory
    :param dir: directory or file to delete
    :return: None
    """
    if os.path.isdir(os.path.join(path, dir)):
        shutil.rmtree(os.path.join(path, dir))
        print("Deleted Directory : " + os.path.join(path, dir))
    else:
        os.remove(os.path.join(path, dir))
        print("Deleted File : " + os.path.join(path, dir))
    return None

Types = {
    "P" : SetPath,
    "D" : DelDirectory,
    "DR" : DelDirectoryRecursively,
    "F" : DelFiles,
    "FR" : DelFilesRecursively,
    "A" : DelAll,
    "AR" : DelAllRecursively,
    "E" : DelEmptyDirectories,
    "ER" : DelEmptyDirectoriesRecursively
}

def UseConfigFiles(lines):
    """
    Delete all files in the list of files to delete
    :return: None
    """
    global path

    for line in lines:
        if line.startswith("#"):
            continue
        lc = line.count(":")
        if lc >= 1:
            split_line = line.split(":")
            arg = split_line[0].strip()
            exp = ':'.join(split_line[1:]).strip()
            if arg in Types.keys():
                    Types[arg](path, exp)
                
            else:
                print("Error in the config file : unknown argument : " + arg)
                continue
        else:
            try:
                DelSimple(path, line.strip())
            except:
                print("Error in the config file : inexistant file or directory : " + line)
                continue
    print("Deletion Ended")

##############################################################################################################
# MAIN

def Main():
    global path
    if os.path.isfile(path + "/config.txt"):
        with open(path + "/config.txt", "r") as configFile:
            lines = configFile.readlines()
        len_lines = len(lines)
    
        i=0
        while i< len_lines and lines[i].startswith("#"):
            i+=1
        if i == len_lines:
            print("Nothing to Do :)")
            exit()
        lines = lines[i:]
        hour = ""
        if lines[0].startswith('H:'):
            lines[0] = lines[0][2:]
            line = lines[0].strip()
            try:
                _ = time.strptime(line, "%H:%M")
            except:
                print("Error in the config file : hour invalid : " + line)
                exit()
            hour = line
            lines = lines[1:]

        if hour == "":
            UseConfigFiles(lines)
        else:
            while True:
                try:
                    given_time = datetime.strptime(hour, "%H:%M")
                except ValueError:
                    raise ValueError("Invalid input format. Please provide time in 'HH:MM' format.")
                current_time = datetime.now()
                target_time = current_time.replace(hour=given_time.hour, minute=given_time.minute, second=0, microsecond=0)

                # If the target time is already in the past, set it to the next day
                if target_time < current_time:
                    target_time += timedelta(days=1)

                time_difference = (target_time - current_time).total_seconds()
                if time_difference - 100 > 0:
                    time.sleep(time_difference - 100)
                do = True
                while do :
                    if datetime.now().strftime("%H:%M") == hour:
                        UseConfigFiles(lines)
                        do = False
    else:
        print("No config file found, creating One...")
        with open(path + "/config.txt", "w") as configFile:
            # write explanations
            configFile.write("# This is the config file for the SimpleFileCleaner.py script\n")
            configFile.write("# If you want to specify an hour where the clean must be executed, ")
            configFile.write("# please use H:XX:XX at the start of the file")
            configFile.write("# You can add files or directories to delete in this file\n")
            configFile.write("# To add a file or directory, just write the path to the file or directory\n")
            configFile.write("# To add a file or directory with a regex, write the regex after the path, separated by a ':'\n")
            configFile.write("# You specify the type of deletion with the first letter of the line then \":\" then the regex\n")
            configFile.write("# The types are :\n")
            configFile.write("# P : Set the path to the directory to clean\n")
            configFile.write("# D : Delete all directories with the regex in the path\n")
            configFile.write("# DR : Delete all directories with the regex in the path and in all subdirectories\n")
            configFile.write("# F : Delete all files with the regex in the path\n")
            configFile.write("# FR : Delete all files with the regex in the path and in all subdirectories\n")
            configFile.write("# Delete all files and directories that match the regex in the path\n")
            configFile.write("# AR : Delete all files and directories with the regex in the path and in all subdirectories\n")
            configFile.write("# E : Delete all empty directories with the regex in the path\n")
            configFile.write("# ER : Delete all empty directories with the regex in the path and in all subdirectories\n")
            configFile.write("# Example :\n")
            configFile.write("# H:03:05")
            configFile.write("# P:C:/Users/username/Desktop\n")
            configFile.write("# D:myDirectory_*\n")
            configFile.write("# P:C:/Users/username/Documents\n")
            configFile.write("# F:myFile_*\n")
            configFile.write("# ER:*\n")
            configFile.write("# \n")
            configFile.write("# Every day, at 3h5 AM :\n")
            configFile.write("# This will delete all directories starting with \"myDirectory_\" in the Desktop directory\n")
            configFile.write("# Then it will delete all files starting with \"myFile_\" in the Documents directory\n")
            configFile.write("# Then it will delete all empty directories in the Documents directory and in all subdirectories\n")
            configFile.write("# And if you don't understand, # Signify that the whole line is a commentary")
        return
    
if __name__ == '__main__':
    Main()
