import json
import os


# Load data from JSON file
def openFile(file_path, default_data=None):
    """
    Opens a JSON file and returns the data as a dictionary.
    If the file does not exist, it creates a new file with default_data if provided.
    If the JSON format is invalid, it returns an empty dictionary or default_data.

    Args:
        file_path (str): Path to the JSON file.
        default_data (dict, optional): Default data to initialize the file if it doesn't exist. Defaults to None.

    Returns:
        dict: Data loaded from the JSON file or default data.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"{file_path} not found. Creating a new one.")
        if default_data is not None:
            saveFile(file_path, default_data)
            return default_data
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON format in {file_path}. Returning default data.")
        return default_data if default_data is not None else {}
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return default_data if default_data is not None else {}


# Save data to JSON file
def saveFile(file_path, data):
    """
    Saves a dictionary as JSON to the specified file path.

    Args:
        file_path (str): Path to save the JSON file.
        data (dict): Data to save.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving to {file_path}: {str(e)}")


# Append data to a JSON file (for lists only)
def appendToFile(file_path, new_data):
    """
    Appends new data to a JSON file if the file contains a list.
    Creates the file with the new data if it does not exist.

    Args:
        file_path (str): Path to the JSON file.
        new_data (dict or list): Data to append.
    """
    try:
        existing_data = openFile(file_path, [])
        if isinstance(existing_data, list):
            existing_data.append(new_data)
            saveFile(file_path, existing_data)
        else:
            print("Error: File content is not a list. Cannot append.")
    except Exception as e:
        print(f"Error appending to {file_path}: {str(e)}")


# Delete JSON file
def deleteFile(file_path):
    """
    Deletes a specified file if it exists.

    Args:
        file_path (str): Path to the file to delete.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully.")
        else:
            print(f"{file_path} does not exist.")
    except Exception as e:
        print(f"Error deleting {file_path}: {str(e)}")


# Update specific key in JSON file
def updateFile(file_path, key, value):
    """
    Updates a specific key-value pair in a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        key (str): Key to update or add.
        value: New value to set for the specified key.
    """
    try:
        data = openFile(file_path, {})
        data[key] = value
        saveFile(file_path, data)
    except Exception as e:
        print(f"Error updating {file_path}: {str(e)}")