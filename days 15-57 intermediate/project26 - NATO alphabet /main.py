# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = pandas.DataFrame(data)
# print(alphabet_df)
# # Loop through rows of a data frame
# for (index, row) in alphabet_df.iterrows():
#      print(row.letter,row.code)

#     # Access row.student or row.score
#     pass
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
print(alphabet_dict)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# alphabet_dict = {letter: code for (letter, code) in alphabet_df.iterrows()}
# print(alphabet_dict)
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("give a word: ").upper()
user_word_list = [letter for letter in user_word] # generate a separate char list form user word

result_list = [alphabet_dict[letter] for letter in user_word_list if letter in alphabet_dict.keys() ]
print(result_list)
