# 🚨 Mail Merge Project 👇

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/5_day(21-25)/Mail Merge Project/Input/Names/invited_names.txt", mode = "r") as f:
    a = f.readlines()
with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/5_day(21-25)/Mail Merge Project/Input/Letters/starting_letter.txt", mode = "r") as letter:
    letters = letter.read()
#Replace the [name] placeholder with the actual name.
for name in a:
    name = name.replace("\n","")
    with open(f"/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/5_day(21-25)/Mail Merge Project/Output/ReadyToSend/{name}.txt", mode = "w") as mail:
        mail.write(letters.replace("[name]", name))
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp