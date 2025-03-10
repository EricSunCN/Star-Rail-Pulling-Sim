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

Examples: 
To access attributes from each part of the JSON file, you need to load the JSON data into a Python object (list of dictionaries) and then use indexing and dictionary key access.

Example:

1. Load the JSON Data

import json

# Load the JSON data from the file
file_path = "standard_5star_characters.json"
data = openFile(file_path)

# Check if data was loaded correctly
if data:
    print("Data loaded successfully!")
else:
    print("Failed to load data.")

2. Access Specific Attributes

a. Access the first character’s name

first_character_name = data[0]["name"]
print(f"First Character Name: {first_character_name}")

Output:

First Character Name: Bronya



⸻

b. Access base stats of a specific character (e.g., Gepard)

gepard_stats = next((char["base_stats"] for char in data if char["name"] == "Gepard"), None)
print("Gepard's Base Stats:", gepard_stats)

Output:

Gepard's Base Stats: {'HP': 1397, 'ATK': 543, 'DEF': 635, 'Speed': 92}



⸻

c. Access a specific ability (e.g., Himeko’s ultimate ability)

himeko_ultimate = next((char["abilities"]["ultimate"] for char in data if char["name"] == "Himeko"), None)
print("Himeko's Ultimate Ability:", himeko_ultimate)

Output:

Himeko's Ultimate Ability: {'name': 'Heavenly Flare', 'type': 'AoE', 'description': 'Deals massive Fire DMG to all enemies.'}



⸻

d. Access all character names

character_names = [char["name"] for char in data]
print("All 5-Star Characters:", character_names)

Output:

All 5-Star Characters: ['Bronya', 'Gepard', 'Himeko', 'Clara', 'Welt']



⸻

e. Access a nested attribute (e.g., Bronya’s skill description)

bronya_skill_description = next((char["abilities"]["skill"]["description"] for char in data if char["name"] == "Bronya"), None)
print("Bronya's Skill Description:", bronya_skill_description)

Output:

Bronya's Skill Description: Dispels a debuff from an ally, allowing them to take action immediately with an ATK boost.



⸻

f. Access a list of characters by element (e.g., all Fire element characters)

fire_characters = [char["name"] for char in data if char["element"] == "Fire"]
print("Fire Element Characters:", fire_characters)

Output:

Fire Element Characters: ['Himeko']



⸻

Example: Combining Multiple Attributes

To print each character’s name, element, and their ultimate ability name:

for char in data:
    print(f"Character: {char['name']}")
    print(f"  Element: {char['element']}")
    print(f"  Ultimate Ability: {char['abilities']['ultimate']['name']}")
    print()

Output:

Character: Bronya
  Element: Wind
  Ultimate Ability: The Belobog March

Character: Gepard
  Element: Ice
  Ultimate Ability: Enduring Bulwark

Character: Himeko
  Element: Fire
  Ultimate Ability: Heavenly Flare

Character: Clara
  Element: Physical
  Ultimate Ability: Promise, Not Command

Character: Welt
  Element: Imaginary
  Ultimate Ability: Synthetic Black Hole



