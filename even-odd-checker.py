#Awfera Python Programming Course Assignment No 01 - Question No 02
def get_valid_number():
    while True:
        user_input = input("Enter a number: ")
        
        # Check if the input contains only digits
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input! Please enter a valid number.")

def check_even_odd(number):
    if number % 2 == 0: #check the reminder is equal to 0 or not when number is divided by 2, if true then the number is even number else the number is odd number.
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

number = get_valid_number()
check_even_odd(number)

