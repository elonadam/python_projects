# given a certain word this code prints a list of NATO alphabet word to help pronunce the letters
#e.g alpha for a, zulu for z
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = pandas.DataFrame(data)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

user_word = input("give a word: ").upper()
user_word_list = [letter for letter in user_word] # generate a separate char list form user word

result_list = [alphabet_dict[letter] for letter in user_word_list if letter in alphabet_dict.keys() ]
print(result_list)
