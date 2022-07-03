import pandas

data = pandas.read_csv('/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/5_day(21-25)/Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray = 0
red = 0
black = 0
for i in data["Primary Fur Color"]:
    if i == "Gray":
        gray += 1
    if i == "Cinnamon":
        red += 1
    if i == "Black":
        black += 1

fur_color = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [gray, red, black],
}
fur_color_data = pandas.DataFrame(fur_color)
fur_color_data.to_csv('/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/5_day(21-25)/Squirrel/fur_color_data')
print(fur_color_data)