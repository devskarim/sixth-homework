from json import load 

try: 
	with open("stundents.json", "r") as f: 
		data = load(f) 
except: 
	print("File not Found") 

tel_phones = list(filter(lambda user: user['phone'].startswith("+998"), data) )

for user in tel_phones: 
	print(f"Name:{user['name']}\nPhone:{user['phone']}\t") 