chai_order = dict(type="Masala Chai",size ="large",sugar="2")
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f'chai recipe { chai_recipe}')

del chai_recipe["liquid"]
print(f"chai recipe: {chai_recipe}")

chai_order = {
    "type":"chai",
    "size": "medium",
    "sugar": 1
}
print(f"Order detials : {chai_order.keys()}")
print(f"order details : {chai_order.values()}")
print(f"order details: {chai_order.items()}")

last_items = chai_order.popitem()
print(f"Last item: {last_items}")

extra_spices = {"cardamom" :"crushed", "ginger": "sliced"}
chai_order.update(extra_spices)
print(f"Updated chai recipe: {chai_order}")

chai_size = chai_order["size"] # size not exist then get the error so use the get method
print(f"Chai size: {chai_size}")

customer_note = chai_order.get("sizes","No note")
print(f"customer_notes is: {customer_note}")