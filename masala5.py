from json import load  

with open("users.json", "r") as f: 
	data = load(f) 

for mail in data: 
	try: 
		if "@" not in mail['email']: 
			raise ValueError (f"Email notog'ri: User: {mail['first_name']}, Mail: {mail['email']}") 
		else: 
			print(f"Good mail : {mail['email']}") 
	except ValueError as e: 
		print(e) 