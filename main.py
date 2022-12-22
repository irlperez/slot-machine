MAX_LINES = 3 # global variable
MAX_BET = 100
MIN_BET = 1


def deposit(): # new function
    while True:
        amount = input('What you would like to deposit? $')
        if amount.isdigit(): # negatives will not be true
            amount = int(amount)

            if amount > 0:
                break # break out of while loop
            else:
                print('Amount must be greater than 0.')

        else:
            print('Please enter a number.')
    
    return amount

def get_number_of_lines():
        while True:
            lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
            if lines.isdigit(): # negatives will not be true
                lines = int(lines)

                if 1 <= lines <= MAX_LINES: # checks if value is in between two values
                    break
                else:
                    print('Enter a valid number of lines.')

            else:
                print('Please enter a number.')
        
        return lines

def get_bet():
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()