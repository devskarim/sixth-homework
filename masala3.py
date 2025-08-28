from json import load 

try: 
	with open("users.json", "r") as mock_data: 
		data = load(mock_data)
		selected = data[:5] 
		print(selected) 
except Exception as e: 
	print("err: ",e) 