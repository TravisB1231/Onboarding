#
# Ask for user first & last name
    #TODO: Name input validation
# Ask for user's division
    #TODO: Present division options
        #TODO: Division input validation

import FDACS_data
confirm = 'n'
while confirm == 'n':
    first_name = input("Enter the user's first name: ")
    last_name = input("Enter the user's last name: ")
    confirm = input(f"You wrote {first_name} {last_name}.\nIs that correct? (Y/N)").lower()
    while confirm != 'y' and confirm !='n':
        confirm = input(f"Incorrect input.\n\nYou wrote {first_name} {last_name}.\nIs that correct? (Y/N)").lower()

for division in FDACS_data.divisions:
    print(division)