from json import load

try: 
	with open("file", "r") as f: 
		data = load(f) 
except ValueError as e: 
	print("File nomi kerak.")