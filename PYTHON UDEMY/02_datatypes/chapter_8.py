"""
List
"""

ingredients = ["water","milk","black tea"]
ingredients.append("sugar")

print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]


chai_ingredients.extend(spice_options)
print(f"Ingredients: {chai_ingredients}")

chai_ingredients.insert(2,"water")
print(f"Ingredients: {chai_ingredients}")


last_added = chai_ingredients.pop()
print(f"Ingredients: {last_added}")


chai_ingredients.reverse()
print(f"Ingredients: {chai_ingredients}")


chai_ingredients.sort()
print(f"Ingredients: {chai_ingredients}")


sugar_level = [1,2,3,4,5]
print(f"Maximu sugar leve: {max(sugar_level)}")
print(f"Minimum sugar level: {min(sugar_level)}")

# overloading
base_liquid  = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["back tea"] * 3
print(f"string brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINN",b"CARD")
print(f"Bytes: {raw_spice_data}")


