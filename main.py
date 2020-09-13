import json, io

def loadData():
        with open("data.json", "r") as read_file:
            data = json.load(read_file)

        return data['CLIENT_ID'], data['SCRIPT_NAME'], data['CLIENT_SECRET']

CLIENT_ID, SCRIPT_NAME, CLIENT_SECRET = loadData()

print(SCRIPT_NAME)
