#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letters:
    start = starting_letters.read()

for name in names:
    clean_name = name.strip('\n')
    new_letter = start.replace("[name]", clean_name)
    print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", mode='w') as output:
        output.write(new_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp