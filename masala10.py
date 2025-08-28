from json import load 

try: 
	with open("users_with_age.json", "r") as f: 
		data = load(f) 
except Exception as e: 
	print("File Not Found")

ages = filter(lambda user: user['age']>= 18, data)

for i in data: 
	print(f"{i['first_name']} - {i['age']}")