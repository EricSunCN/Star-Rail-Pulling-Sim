import json

def openFile(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File not found.")
        return {}  # Return an empty dictionary or handle it as needed
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return {}  # Return an empty dictionary or handle it as needed
    #This is still under development, DO NOT call this function, it leaks memory.