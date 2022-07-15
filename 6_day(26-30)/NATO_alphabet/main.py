import pandas
data = pandas.read_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/NATO_alphabet/nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
name = input("What's your name?: ").upper()
a = [data_dict[f"{letter}"] for letter in name]
print(a)