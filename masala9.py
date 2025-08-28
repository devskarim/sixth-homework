from json import load 

try: 
		with open("numbers.json") as data: 
			numbers = load(data)
			datas = sum(map(int, numbers)) 
			print("total: ", datas) 
except ValueError as e: 
	print("there is value wich is not int ") 

