import os
starting_letters_path = r"D:\Python\Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt" 
invited_names_path = r"D:\Python\Day 24\Mail Merge Project Start\Input\Names\invited_names.txt"
output_ready_to_send_path = r"D:\Python\Day 24\Mail Merge Project Start\Output\ReadyToSend"


# Replacing the names.
with open(starting_letters_path) as letters_file:
    read_letters_file = letters_file.read()

with open(invited_names_path) as invited_names:
    split_names = invited_names.read().splitlines()

for name in split_names:
    updated_letter = read_letters_file.replace("[name]", name) 
    # print(updated_letter) # for checking uncomment.


    file_name = f"letter_for{name}.txt"
    output_path = os.path.join(output_ready_to_send_path, file_name)

    with open(output_path, mode = "w") as output_file:
        output_file.write(updated_letter)
    print(f"saved: {output_path}")


# # Reading the file.
# with open(starting_letters_path, mode = "r") as file:
#     content = file.read()
#     print(content)

# # Storing the names into a varaible.
# with open(invited_names_path) as name_file:
#     split_names = name_file.read().splitlines()    
#     for name in split_names:
#         print(name)



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp