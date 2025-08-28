from json import load 

try: 
	with open("stundents.json", "r")  as f: 
		data = load(f) 
except:
	print("File topilmadi.")

aGPA = filter(lambda gpa: gpa['GPS'] >=3.0, data) 

for user in aGPA: 
	print(f"Name: {user['name']} - {user['GPS']}") 