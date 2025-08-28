from json import load 

try: 
	with open("data.json", "r") as f: 
		data = load(f)
		print(data)
except: 
	print("File Not Found")