"""Writing for loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]

GoodBoy: list[str] = []

for elem in pets:
    print("Good boy, " + elem + "!")


"""Practice with for loops + functions."""

def even_words(inp_list: list[str]) -> list[str]:
    """What it does is a mystery!;)"""
    even_list: list[str] = []
    for elem in inp_list:
        if len(elem) % 2 == 0:
            even_list.append(elem)
    return even_list


a: list[str] = ["Alyssa", "Katie", "Anusha"]
even_words(a)
