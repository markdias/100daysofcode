# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

from pickle import FALSE, TRUE
import pandas

data = pandas.read_csv("day-30-start/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_good = True


while is_good:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet')
    else:
        print(output_list)
        is_good = False
    finally:
        if not is_good:
            print('Thank you for using NATO Convertor')        
