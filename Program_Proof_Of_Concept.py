# proof of concept 1.0
# Jack Bell
# 28/12/2022

import sys
# inport the system this allows for "sys.stdout.write" & "sys.readline"

# createing a function that displays the record
def display_record(file):
    file = open(file, "r")
    # ^ opens the file in 'read mode' 
    file = file.read()
    sys.stdout.write(file)
    # Line 13 and 14 will print the contents of the .txt file

# createing a function that allows the user to add to a recprd
def add_to_record(txt_file):
    with open(txt_file,"a") as file:
        # ^ opens the file in 'edit mode' 
        sys.stdout.write("what do you want to write? ")
        # ^ ask the user what they want to add to the .txt file 
        file.write(input() + "\n")
        #wites the input to the .txt file
        file.close()
        #closes the .txt file



#Start of user menu
message ="Welcome, This program will print data in to .txt file and or display this infomation on the .txt file, Made for ages 8-12\n"
message +="\n"
message +="Type 1 to Add a record: \n"
message +="Type 2 to Display records: \n"
message +="Type 3 to Exit: \n"
message +="Whats your option: "
sys.stdout.write(message)
#prints the above menu
#End of user menu

user_input = int(sys.stdin.readline())
#take input form the user form menu



#Calling requird function 
if user_input == 1:
    message1 ="what file: try 'test_case.txt' : "
    # ^ show the user what input to use
    sys.stdout.write(message1)
    # ^ print the message
    file1 = input()
    add_to_record(file1)
    # ^ call the function
elif user_input == 2:
    message2 ="what file: try 'test_case.txt' : "
    # ^ show the user what input to use
    sys.stdout.write(message2)
    # ^ print the message
    file2 = input("what file: try 'test_case.txt' : ")
    display_record(file2)
    # ^ call the function
else:
    exit()
#Exit the program