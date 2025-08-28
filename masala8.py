from json import load 

try: 
	with open("product.json", "r") as js_file: 
		data = load(js_file) 
except ValueError	as e: 
	print(e) 
else: 
	for product in data: 
		print(f"Name: {product['name']}\nPrice: {product['price']}\n") 
