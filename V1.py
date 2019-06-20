#Eyatar Nezer
#Daniel Levy

import re

filePath = "C:\\Users\\danielle\\Desktop\\vpnd.elg"
file = None

print("Program started")

def parse_file(file, filePath, mode):
    file = open(filePath, mode)

    line = file.readline()
    pid = extract_pid(line)
    print("PID: " + pid)

def extract_pid(line):
    return re.search("\s*\d{3,}\s", line, flags=0).group().strip()

parse_file(file, filePath, "r")
