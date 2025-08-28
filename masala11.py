from json import load 

try: 
	with open("numbers.json", "r") as f: 
		data = load(f) 
except: 
	print("File not Found") 

num_degre = list(map(lambda x: x*x, data)) 

print(num_degre) 