"""Some functions for my garden plan!"""

__author__ = "730418328"

# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Mutating Input Dictionary."""
    if new_plant_kind in by_kind:  # if kind is already in dictionary ("flower" was in by_kind, so I did this step)
        by_kind[new_plant_kind].append(new_plant)  # to access the list 
        # want to get: {"flower": ["marigold", "zinnia", "dairy"], "vegetable: ["carrots"]"}
    else:  # if kind is not in dictionary ("fruit is not in by_kind")
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)
    

def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in garden_by_date:  # april: [this, that], may: [over, there]
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Searches through dictionaries and returns a list of plants to plant in correct month."""
    assert kind in plants_by_kind  # have to make this condition because if the kind doesn't exist
    assert month in plants_by_date
    list_kind: list[str] = plants_by_kind[kind]  # receiving those values of that kind in a new variable - list of plants of a kind 
    list_month: list[str] = plants_by_date[month]  # receiving values of plants to grow in specific month 
    # now want to go through both lists and find elements that appear in both
    combined_list: list[str] = []
    for plant in list_kind:  # looking at first element in the list kind and testing it against all the elements of list month
        for other_plant in list_month:
            if plant == other_plant:
                combined_list.append(other_plant)
        # print(flowers to plant in <month>: <combined list>)
        
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {kind}s to plant in {month}."