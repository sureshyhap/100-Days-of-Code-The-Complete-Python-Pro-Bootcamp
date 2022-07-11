import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_count_dict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [0, 0, 0]
}
for color in data["Primary Fur Color"]:
    if color == "Gray":
        fur_count_dict["Count"][0] += 1
    elif color == "Cinnamon":
        fur_count_dict["Count"][1] += 1
    elif color == "Black":
        fur_count_dict["Count"][2] += 1
pandas.DataFrame(fur_count_dict).to_csv("fur_count.csv")