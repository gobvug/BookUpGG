'''
Gerald Gobvu
HI50306X
'''


while True:

    print("Enter 'x' if you want to exit.")

    #prompts user to enter statement and stores it in variable 'string'
    string = input("Enter your string: ")

    #checks whether string is x if not it prints length of the string
    if string == 'x':
        break
    else:
        print("Length of string =", len(string), "\n")


