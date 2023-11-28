# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./input/Letters/starting_letter.txt") as file:
    templet = file.read()

with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

for name in names:
    name_without_space = name.strip()
    templet_del = templet.replace("[name]", name_without_space)
    with open(f"./output/ReadyToSend/letter_to_{name_without_space}.txt", "w") as file_ready:
        file_ready.write(templet_del)
