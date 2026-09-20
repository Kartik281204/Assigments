import pandas as pd  # type:ignore

calories = {"Day 1": [2000, 2000, 2000], "Day 2": [500, 500, 500], "Day 3": [
    1000, 1000, 1000], "Day 4": [29903, 29903, 29903]}

menu = pd.DataFrame(calories, index=["pizza", "pasta", "burger"])
menu["Day 5"] = [2000, 2000, 2000]
menu.loc["salad"] = [1000, 2000, 3000, 4000, 5000]

new_list = pd.DataFrame([{"Day 1": 55000, "Day 2": 45000,
                         "Day 3": 35000, "Day 4": 25000, "Day 5": 15000}], index=["chicken"])
menu = pd.concat([menu, new_list])

print(menu)
