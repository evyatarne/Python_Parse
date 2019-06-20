#Eyatar Nezer
#Daniel Levy

filePath = "C:\\Users\\danielle\\Desktop\\vpnd.elg"
file = None

print("Program started")

def open_file(file, filePath, mode):
    file = open(filePath, mode)

open_file(file, filePath, "a")
