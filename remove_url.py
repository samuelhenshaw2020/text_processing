import re
import sys

if sys.argv[1] == "":
    raise Exception("No argument provided for target file")
# if sys.argv[2] == "":
#     raise Exception("the flag '--line-space=yes|no' is compulsory")


is_space = False
# print(sys.argv[2].split("=")[1])

print("parsing file: " + sys.argv[1])


pattern = "https?:\/\/(?:[-\w.]|(?:%[\da-fA-F]{2})|\/)+"

# f = open(sys.argv[2], "w")

textData = ""

try:
    # print(sys.argv[2] + " created")
    print("parsing file: " + sys.argv[1])
    with open(sys.argv[1]) as file:
            for line in file:
                text = re.sub(pattern, "" , line)
                textData += f"{text}"
except FileNotFoundError:
    raise FileNotFoundError(f"{sys.argv[1]} not found")
            

try:
    f = open(sys.argv[1], "w")
    f.write(textData)
except:
    raise Exception("Issues while writing to a")
finally:
    f.close()


print("URLs removal done!")
            