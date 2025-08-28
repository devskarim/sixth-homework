from json import  load 
try:
	with open("data.json", "r") as f:  
		data  = load(f)
		print(data)
except Exception as e: 
	print("Fayl buzilgan yoki Mavjud emas.", e) 