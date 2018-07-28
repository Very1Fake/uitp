# UiTP LightPixel copyright 2018 GNU GPL-3.0
# v0.0.0a1

import json

class Protocol():
    def __init__(self):
        pass

    def getMsgFromString(self, string, encoding='utf-8'):
        msg = bytes(string, encoding)
        return msg

    def getMsgFromArray(self, array, encoding='utf-8'):
        string = json.dumps(array)
        msg = bytes(string, encoding)
        return msg


class Universal(Protocol):
    def __init__(self):
        pass
    
    def sendMsg(self, ip, port):
        pass
