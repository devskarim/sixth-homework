num = list(map(int, input("Sonlar kiriting: ex(1,2,..): ").split(",")))

juft_son = list(filter(lambda x: x%2==0, num)) 
toq_son = list(filter(lambda x: x%2 != 0, num)) 

print("Juft sonlar: ", juft_son) 
print("Toq sonlar: ", toq_son) 