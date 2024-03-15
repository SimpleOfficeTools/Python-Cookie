# Check the IO docs before release:
while True:
    # take input from the user
    choice = input("Enter choice: Create/edit or View ")

    # check if choice is one of the four options
    if choice in ('Create/edit', 'View',):
        File = (input("Enter filename "))


        if choice == 'Create/edit':
            Edits = input('Enter your edits')
            with open(File, 'w') as f:
             f.write("Hello, world!\n")
             f.write(Edits)
             

        elif choice == 'View':
            with open(File, 'r') as f:
             content = f.readlines()
             print(content)