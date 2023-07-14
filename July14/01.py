from json import *

# data =  '{"type": "forecast","duration": 3,"city": "karaganda","counry_code": "kz"}'

# request = loads(data)
# request['city'] = "almaty"
# data = dumps(request, ensure_ascii = False)

with open("01_input.txt",  encoding="utf-8") as myfile:
    request = load(myfile)

request['city'] = "almaty"



with open("01_input.txt", "w", encoding="utf-8") as myfile:
    dump(request, myfile)
