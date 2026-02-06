class Age:
    @staticmethod
    def check_age(age):
        if age < 18:
            return "Minor"
        else:
            return "Adult"

print(Age.check_age(15))
print(Age.check_age(25))