# Boolean


is_boilling = True
stri_count = 5 
total_actions = stri_count + is_boilling  # upcasting   see as 1 
print(f"Total actions: {total_actions}") 


milk_present = None    # "hitesh"  # no milk
print(f"Is there milk? {bool(milk_present)}")


# and , or , not 


water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"can server chai ? :{can_server} ")


can_server = water_hot or tea_added
print(f"can server chai ? :{can_server} ")


print(f"can server chai ? : {not(can_server)} ")