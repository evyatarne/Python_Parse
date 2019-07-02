#Eyatar Nezer
#Daniel Levy
#Hare Krishna

import re

filePath = "C:\\Users\\danielle\\Desktop\\vpnd.elg"

print("Program started")


def parse_file(filePath, mode):
    with open(filePath, mode) as f:
        #line = f.readline()
        for i, line in enumerate(f):
            pid = extract_pid(line)
            print("PID: " + str(pid))


# Gets the pid from the line
# Assuming pid is not more than 6 characters
def extract_pid(line):
    pid = re.search("\\s*\\d{3,}\\s", line, flags=0)
    if pid is not None:
        if count_characters(pid.group().strip()) <= 6:
            return pid.group().strip()


# Returns the number of characters in a string
def count_characters(string):
    count = 0
    for c in string:
        count += 1
    return count


parse_file(filePath, "r")
