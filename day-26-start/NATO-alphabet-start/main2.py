import pandas

nato_alphabet_df = pandas.read_csv("day-26-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")

df = {row.letter:row.code for (index, row) in nato_alphabet_df.iterrows()}

word  = input("Enter a word: ").upper()


nato_names = [df[letter] for letter in word]

print(nato_names)