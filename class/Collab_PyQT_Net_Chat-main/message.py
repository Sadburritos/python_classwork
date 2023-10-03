import json


class Message():
    time = 0
    senderName = ""
    text = ""
    receiverName = ""
    type = ""

    def __init__(self, jsonstring) : # '{"time": "03-10-2023}:
        data = json.loads(jsonstring)
        self.time = data.get("time" , "")
        if "senderName" in data:
            self.senderName = data["senderName"]
        if "text" in data:
            self.text = data["text"]
        if "receiverName" in data:
            self.receiverName = data["receiverName"]
        if "type" in data:
            self.type = data["type"]


    def toJson(self):
        data = {}
        data["time"] = self.time
        data["text"] = self.text
        data["type"] = self.type
        data["senderName"] = self.senderName
        data["receiverName"] = self.receiverName
        return json.dumps(data)


if "__main__" == __name__:
    msg = Message("text:sendername")