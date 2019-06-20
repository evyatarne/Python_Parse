#Eyatar Nezer
#Daniel Levy

import re

filePath = "C:\\Users\\danielle\\Desktop\\vpnd.elg"
file = None

print("Program started")

def open_file(file, filePath, mode):
    file = open(filePath, mode)

    line = file.readline()
    pid = re.search("\s*\d{3,}\s", line, flags=0).group()
    print("PID:" +  pid)

open_file(file, filePath, "r")
