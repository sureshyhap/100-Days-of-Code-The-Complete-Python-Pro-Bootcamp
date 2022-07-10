#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    with open("Input/Names/invited_names.txt") as invited_names:
        list_of_names = invited_names.readlines()
        for name in list_of_names:
            name = name.strip()
            correct_output = letter.replace("[name]", name)
            with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as new_file:
                new_file.write(correct_output)