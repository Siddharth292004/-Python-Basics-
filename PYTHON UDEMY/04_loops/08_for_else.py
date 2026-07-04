staff = [("Amit", 15), ("Zera", 12), ("Raj", 18)] 

for name,age in staff:
    if age >=18:
        print(f"{name} is eligible to manage the staff")
else:
    print(f"No one is eligible to manage the staff")
