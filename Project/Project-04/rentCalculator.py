# inputs we nee from the user
# total rent
# Total food ordered for snacking 
# Electricity units spend
# charge per unit 

## output 
# Totoal amount you have to pay


rent = int(input("Enter your hostel rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of eletricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter number of persons living in room = "))

total_bill = electricity_spend * charge_per_unit

total_amount_spend = (rent + food + total_bill) / persons

print(f"Each person will pay = {total_amount_spend}")
