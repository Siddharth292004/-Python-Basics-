#9️⃣ Calculate simple interest using class.

#🔹 Hint:

#Formula: SI = (P × R × T) / 100

#Use method to calculate

class Interest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time
    
    def calculate_simple_interest(self):
        si = (self.principal * self.rate * self.time) / 100
        return si

Interest1 = Interest(1000, 5, 3)
simple_interest1 = Interest1.calculate_simple_interest()
print(f"Simple Interest for first object: {simple_interest1}")
Interest2 = Interest(2000, 7, 2)
simple_interest2 = Interest2.calculate_simple_interest()
print(f"Simple Interest for second object: {simple_interest2}")
