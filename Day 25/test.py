"""
with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)



import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    first_row = True
    for row in data:
        if first_row:
            first_row = False
            continue
        temperatures.append(int(row[1]))
    for temp in temperatures:
        print(temp)


import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
print()
print(type(data["temp"]))
print(type(data))


data_dict = data.to_dict()
print(data_dict)

data_temp = data["temp"]
print(data_temp.mean())
data_temp_list = data_temp.to_list()


avg_temp = sum(data_temp_list) / len(data_temp_list)
print("{:.2f}".format(avg_temp))

print(data_temp.max())
print(data.temp)


print(data[data.day == "Monday"])
max_temp = data["temp"].max()
print(data[data.temp == max_temp])


monday = data[data.day == "Monday"]

def celsius_to_fahrenheit(temp):
    return temp * (9 / 5) + 32

print(celsius_to_fahrenheit(float(monday.temp)))

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("weather_data.csv")
print(len(data))
print(type(data[data.day == "Monday"]))
"""