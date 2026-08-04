favourite_chais = [
    "Masala Chai","Green tea","Masala Chai",
    "Lemon Tea","Green Tea","Elaichi Chai"
]

unique_chai = { chai for chai in favourite_chais if len(chai) > 8}
print(unique_chai)

