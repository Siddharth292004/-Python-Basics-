#🔟 Accept marks and calculate total & percentage.

#🔹 Hint:

#Take marks as input

#Total = sum of marks

#Percentage = (total / max) × 100

class StudentMarks: 
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def calculate_total_and_percentage(self):
        total = self.mark1 + self.mark2 + self.mark3
        percentage = (total / 300) * 100
        return total, percentage
    
student1 = StudentMarks(85, 90, 78)
total1, percentage1 = student1.calculate_total_and_percentage()
print(f"Student 1 - Total: {total1}, Percentage: {percentage1:.2f}%")