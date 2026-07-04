flavours = ["Ginger","Out of Stock","Lemon","Discountinued","Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discountinued":
        break
    print(f"{flavour} item found")

print(f"Out side of loop")
