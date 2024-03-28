"""Practice with Dictionaries and for Loops."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    #name of the dictionary is key
    #subscription notation to enter the value of the key
    print(in_stock[key])
    #it'll print the bool of each key...so if we only want it to print if it's True...
    if in_stock[key] == True:
        or 
    if in_stock[key] is True:
        or 
    if in_stock[key]: #don't need to put is True, it's already checking to see if it's True 
        print(key)