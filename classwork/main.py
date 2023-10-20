import sys
import json


print(sys.argv)
args = sys.argv


config = {}

for i, a in enumerate(args[:-1]):
    if a == "--text" or a == "-t":
        config["text"] = args[i+1]
    if a == "--debuglevel" or a == "-d":
        config["debuglevel"] = args[i+1]
    if a == "--mode" or a == "-m":
        config["mode"] = args[i+1]
    if a == "--output " or a == "-o":
        config["output"] = args[i+1]
print(config)
