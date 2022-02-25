import re
import sys

if sys.argv[1] == "":
    raise Exception("No argument provided for target file")
if sys.argv[2] == "":
    raise Exception("No argument provided for destination file")

pattern = "(#+[a-zA-Z0-9(_)]{1,})"

f = open(sys.argv[2], "w")

try:
    print(sys.argv[2] + " created")
    print("parsing file: " + sys.argv[1])
    with open(sys.argv[1]) as file:
            for line in file:
                text = re.sub(pattern, "" , line)
                try:
                    f.write(text)
                except:
                    raise Exception(f"Something went wrong while trying to write to {sys.argv[2]} file")
except FileNotFoundError:
    raise FileNotFoundError(f"{sys.argv[1]} not found")
finally:
    f.close()
            

print("parsing done!")
            