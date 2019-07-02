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
def extract_pid(line):
    pid = re.search("\\s*\\d{3,}\\s", line, flags=0)
    if pid is not None:
        return pid.group().strip()


parse_file(filePath, "r")
