#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open(r"Day 24\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()
    
    

with open("Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter = starting_letter.read()
    for ind, name in enumerate(names,start=1):

        
        clean_name = name.strip()
        letter_body = letter.replace("[name]",clean_name)
        
        file = open(f"C://100-days-of-python-learning//Day 24//Mail Merge Project Start//Output//ReadyToSend//letter_for_{clean_name}.txt" , 'w')

        file.write(letter_body)

        file.close()
        