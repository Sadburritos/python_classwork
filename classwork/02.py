import json
import os
import sys

default_config = {'text': 'filename.txt', 'debuglevel': 'warning', 'mode': 'delayed', 'output': 'stdout'}
with open("config.json") as fp:
    new_conf = json.load(fp)

for key in default_config:
    if key in new_conf:
        default_config[key] = new_conf[key]

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

for key in default_config:
    if key in config:
        default_config[key] = config[key]

print(default_config)
