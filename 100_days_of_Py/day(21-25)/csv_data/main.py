import pandas

data = pandas.read_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/day(21-25)/csv_data/weather_data.csv")

# csv to dictionary
data_dict = data.to_dict()
print(data_dict)

# csv to list
data_list = data["temp"].to_list()
print(data_list)

# Average temperature
print(f"Average temperature = {round(sum(data_list)/len(data_list), 2)}")
# same as above
print(data["temp"].mean())

# Max temperature
print(data["temp"].max())

# Get data in Columns
print(data["condition"]) # equal to print(data.condition)

# Get data in Row
print(data[data.day == "Monday"])

# Get data in Row with max temperature
print(data[data.temp == data.temp.max()])

# Filter data in row
monday = data[data.day == "Monday"]
print(monday.condition)
fahrenheit = (monday.temp * 1.8) + 32
print(fahrenheit)

# Create dataframe from scratch
data_dict = {
    "student": ["Amy", "John", "Thomas"],
    "score": [76, 56, 90],
}
data = pandas.DataFrame(data_dict)
data.to_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/day(21-25)/csv_data/new_data.csv")
print(data)