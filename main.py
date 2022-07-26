#TODO: Create a letter using starting_letter.docx 

#In this program we want to make letters from default letter and just subtitute the name of our guest by using
#File Directory
#First we want to take the list of our guest to the party from invted_names.txt
with open("Input/Names/invited_names.txt") as file_name:

     list_names = (file_name.readlines())
#Then we extract the default text of our letter
     with open("Input/Letters/starting_letter.docx") as let :
         letter_text = let.read()




     for name in list_names:
         #Remove the spaces besides names inside our list_names by strip() method
         letter_name = name.strip()


       #Replace the name of our guest instead of [name] by replace("old","new") method
         with open(f'Output/ReadyToSend/{letter_name}.txt', mode= "w") as letter:
             new = letter_text.replace("[name]", f"{letter_name}")
             letter.write(new)















