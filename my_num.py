def pick_big():
    n1 = int(input("Enter 1st number"))
    n2 = int(input("Enter 2nd number"))
    if n1>n2 : 
          print("n1 is bigger" , n1)
    elif n2>n1: 
         print("n2 is bigger" , n2)
    else:
        print("the numbers are equal ")

def pick_small():
    n1 = int(input("Enter 1st number"))
    n2 = int(input("Enter 2nd number"))
    if n1<n2 : 
          print("n1 is smaller" , n1)
    elif n2<n1: 
         print("n2 is smaller" , n2)
    else:
        print("the numbers are equal ")

def run_number_loop():
    number = 0
    
    while True:
        user_input = input(f"Current number: {number}. Press Enter to continue or type 'x' to exit: ")
        
        if user_input.lower() == 'x':
            break
        
        number += 1

# Call the function to start the loop

