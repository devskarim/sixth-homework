from json  import load 

with open("users.json", "r") as f: 
	data = load(f) 


for user in data: 
	try: 
			if user['age'] < 0: 
				raise ValueError(f"Age notogri. User: {user['first_name']} {user['age']}")
			else:
					print(f"True user: {user['first_name']} age: {user['age']}")
	except Exception as e:
		print("err", e) 