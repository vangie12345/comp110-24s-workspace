"""Practice with dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)


#Removing 
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#Accessing/Modifying
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Checking if in dictionary
print("mint" in ice_cream)

ice_cream["pecan"]




def add_player(record: dict[str, float], name: str, avg: float) -> None:
    record[name] = avg
    print("add")

d: dict[str, float] = {"Cobb": .366, "Ruth": .342}
add_player(d, "Gehrig", .340)
print(d)