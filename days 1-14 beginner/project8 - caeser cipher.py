#8/100 days of coding, Caesar cipher
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

# to add option to insert full sentences

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP'''"""""""'''  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                                                           
           ##             88                                 
           ""             88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP'''"""""""''' 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
user_answer = 'yes'
while user_answer == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction != 'encode' and direction != 'decode':
    print("Please try again, encode / decode was typed wrong")
    exit()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def encrypt_decrypt (text_list, shift):
    encrypt_text = ""
    if direction == 'decode':
      shift *= -1
    for letter in text_list: 
      letter_place = alphabet.index(letter) # the letter curr index
      shifted_letter = alphabet[(letter_place + shift) % 26]
      encrypt_text += shifted_letter
    print(f"the {direction} result is: " + encrypt_text) 

  encrypt_decrypt(text,shift)
  user_answer = input("Do you want to try again ? write yes / no\n").lower()
