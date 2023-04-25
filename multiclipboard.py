import sys
import clipboard
import json 

SAVED_DATA = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
#save_items("clipboard.json", {"Data" : "value"})

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}

#data = clipboard.paste()
#print(data)

#clipboard.copy("sani")

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)
    
    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)

    elif command == "load":
            key = input("enter a key: ")
            if key in data:
                clipboard.copy(data[key])
            else:
                print("Key does not exist")

    elif command == "list":
        print(data)
    else:
        print("Invalid command")
else:
    print("Please pass exactly one command")
