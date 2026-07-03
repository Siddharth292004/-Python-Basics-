"""
Set: 
"""

essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")


common_spices = essential_spices & optional_spices
print(f"common: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")


print(f"Is 'cloves' in optional spices :{'cloves' in optional_spices}")