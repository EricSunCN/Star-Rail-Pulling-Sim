Functions

1. openFile(file_path, default_data=None)

What it does:
Opens a JSON file and returns the data. If the file doesn’t exist, it creates one with the default data if provided. If the file is broken, it returns the default data or an empty dictionary.

What it needs:
	•	file_path (str): Where the file is.
	•	default_data (dict, optional): Starting data if the file isn’t there. Defaults to None.

What it returns:
	•	A dictionary with the file data or default data.

Example:

data = openFile("data.json", {"default": "value"})
print(data)



⸻

2. saveFile(file_path, data)

What it does:
Saves a dictionary as JSON to the given file path.

What it needs:
	•	file_path (str): Where to save the file.
	•	data (dict): Data to save.

Example:

saveFile("data.json", {"name": "Alice", "age": 30})



⸻

3. appendToFile(file_path, new_data)

What it does:
Adds new data to a JSON file if it has a list inside. It creates a new file if it doesn’t exist.

What it needs:
	•	file_path (str): Where the file is.
	•	new_data (dict or list): Data to add.

Example:

appendToFile("data.json", {"task": "Buy milk"})



⸻

4. deleteFile(file_path)

What it does:
Deletes the file if it’s there.

What it needs:
	•	file_path (str): Where the file is.

Example:

deleteFile("data.json")



⸻

5. updateFile(file_path, key, value)

What it does:
Changes or adds a specific key-value pair in a JSON file.

What it needs:
	•	file_path (str): Where the file is.
	•	key (str): Key to change or add.
	•	value: New value for that key.

Example:

updateFile("data.json", "age", 31)



⸻

Error Handling
	•	If a file is missing, broken, or can’t be read or written, the functions print error messages.
	•	This helps to understand what went wrong.
