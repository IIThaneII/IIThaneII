# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/NATO_alphabet_2.0/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
a = True
while a:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        a = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
