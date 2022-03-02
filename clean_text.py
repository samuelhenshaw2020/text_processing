import re 
import sys

# GET COMMAND LINE PARAMETER
try:
    linespace = sys.argv[1] # --line-space=yes|no 
    filepath = sys.argv[2]
except:
    raise Exception("argument 'file' or 'linespace' is missing")

data = ""

# GENERATE LINE SPACE
linespace = True if linespace.split('=')[1] == "yes" else False
filepath = filepath.strip()


try:
    with open(filepath) as file: # Open the text document for reading
        lines  = [t.strip() for line in file for text in line.strip().split("\n") for t in text.split('.') if t.strip() != '']
        for i in lines:
            if i.strip().endswith('.') or i.strip().endswith('?'):
                data += f"{i}\n\n" if linespace == True else f"{i}\n"
            else:
                data += f"{i}.\n\n" if linespace == True else f"{i}.\n"
except:
    print("somsthing went wrong while writing to file")
    raise Exception("")



try:
    f = open(filepath, mode="w")
    f.write(data)
except:
    print("somsthing went wrong while writing to file")
    raise Exception("")