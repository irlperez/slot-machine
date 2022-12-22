import random 

MAX_LINES = 3 # global variable
MAX_BET = 100
MIN_BET = 1

# number rows and columns in slot machine
ROWS = 3
COLS = 3

# how many symbols in each column (aka reel)
symbol_count = { # dictionary of symbols, key is the symbol: count of each symbol
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}

def get_slot_machine_spin(rows, cols, symbols:dict):
    
    all_symbols = []

    # First for loop gets the symbol and the count. Second for loop goes threw n (n = count) times of that symbol and appending the symbol to the list above.
    for symbol, symbol_count in symbols.items(): # .items() returns both the key and the value
        # unused variable syntax https://peps.python.org/pep-0640/ -- people also use unused
        for _ in range(symbol_count): 
            all_symbols.append(symbol)


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
    while True:
        amount = input('What you would like to bet on each line? $')
        if amount.isdigit(): # negatives will not be true
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break # break out of while loop
            else:
                print(f'Amount must be between {MIN_BET} - {MAX_BET}.') # f-string

        else:
            print('Please enter a number.')
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
        else:
            break
    
    print(f'You are betting ${bet} on {lines}. Total bet is equal to ${total_bet}')

    # print(balance, lines)


def test():
    print(get_slot_machine_spin())

main()