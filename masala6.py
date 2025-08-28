from json import load 

with open ("product.json", "r") as pr: 
	data = load(pr) 

for pris in data: 
	try: 
		if not isinstance(pris['price'], int): 
			raise TypeError(f"Price int bolishi kerak. {pris['price']}") 
		else: 
			print(f"name: {pris['name']}\nprice:{pris['price']}") 
	except TypeError as e: 
		print("Error", e)