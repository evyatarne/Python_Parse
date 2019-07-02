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
            print("PID: " + pid)


#Gets the pid from the line
def extract_pid(line):
    return re.search("\s*\d{3,}\s", line, flags=0).group().strip()


parse_file(filePath, "r")
