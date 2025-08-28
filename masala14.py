from json import load  

try: 
	with open("numbers.json", "r") as f: 
		data = load(f) 
except: 
	print("File not Found")  


couple_numbers = filter(lambda x: x%2==0, data)

for num in couple_numbers: 
	print(num)