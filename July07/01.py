config = {}


cfg_file = open("config.ini", encoding="UTF-8")
my_config = cfg_file.readlines()
cfg_file.close()

for x in my_config:
    res = x.split("=")
    res[0] = res[0].strip()
    res[1] = res[1].strip()

    if res[1].lower in ["true", "yes", "on"]:
        res[1] = True
    elif res[1].lower == ["false", "no", "off"]:
        res[1] = False
    elif res[1].isdigit():
        res[1] = int(res[1])
    config[res[0]] = res[1]


print(config)