names = ["hitesh","Meera","Sam", "Ali"] 
bills = [50,60,70,80,90]

for name,amount in zip (names,bills):
    print(f"{name} paid {amount} rupees")