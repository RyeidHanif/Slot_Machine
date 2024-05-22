#slot machine . allows the user to bet on a line of slots . if all 3 same in one line , user wins some money 
# if different user loses all what they wanted to 
# allow them to continue until they want to quit or they run out of money 


#startingwith collect some user input 

import random 
import time 

#imagine have 3 by 3 slot machine

ROWS = 3
COLS = 3

#specify how mant symbols in each of the reels (column)
# for now ABCD will be the symbols

MAX_LINES = 3
MAX_BET =  100
MIN_BET = 1

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value= {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

#generate outcome of slot machines 

def get_slot_machine_spin(rows,cols,symbols):
    #randomly select values for each of our columns
    #create list of all possible , and randomly choose 3
    
    all_symbols = []
    for symbol,symbol_count in symbols.items(): #dictionary fun
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    
    #here each nested list will store the columns 
    #columns = [[], [] , []]
    # we will use a copy of that list so once we have a letter , we can remove it without affecting the origianl list
    
    columns =[]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # how to copy a list
        for  _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

#columns is the bgi array , column are the inner arrays, fill column with3 rows then append it to columns


def print_slot_machine(columns):
    #not in an easy format to print
    #currently the rows are columns and columns are rows 
    # now this is transposign ti 

    for row in range(len(columns[0])): # finding the length of the column to male it rows 
        for i , column in  enumerate(columns):
            if i != len(columns) - 1 :  
             print(column[row], end = "|")
            else : 
                print(column[row] , end = "")
        print() # brings us to next line





def deposit():
    while True:
        amount = (input("what would you like to deposit ? : $"))
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else : 
                print("AMOUNT  must be greater than 0 ")
        else:
            print("Error , enter valid amount")
    return amount

#calculate their bet amount and number of lines and how much bet

def get_number_of_lines():
    while True:
        lines = (input(f"Enter number of lines to bet on (1 - {str(MAX_LINES)} : "))
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else : 
                print("enter valid no of lines ")
        else:
            print("error , enter valid number " )
    return lines


#amount to bet on each line
def get_bet():
    while True:
        bet_amount = (input("what would you like to bet  on each line? : $"))
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET :
                break
            else : 
                print(F"Bbet must be between {MIN_BET} and {MAX_BET}")
        else:
            print("error , enter a proepr number for a bet")
    return bet_amount


#betting on 1 line is top ine , 2 is both and 3 is all
def check_winnings(columns , lines , bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): 
        symbol = columns[0][line] # we look at the first column and then the row according to the line
        for column in columns:
            symbol_to_check = column[line]
            if symbol!= symbol_to_check:
                break
        else : 
            winnings += values[symbol] * bet #key value pair of dictionary
            winning_lines.append(line + 1) # dont want index, want actual numer
    return winnings , winning_lines


def spin(balance):
  lines = get_number_of_lines()

 #have to check if bet is within balance range
  while True:
   bet = get_bet()
  
   total_bet = bet * lines
   if total_bet > balance : 
      print(f"You do not have enough balance to bet that amount your current balance is ${balance}")

   else : 
      break

  print(f"you are betting ${bet} on {lines} lines . total bet is equal to ${total_bet}")
  
  slots = get_slot_machine_spin(ROWS , COLS , symbol_count)
  print_slot_machine(slots)
  winnings  , winning_lines= check_winnings(slots , lines , bet , symbol_value)
  print(f"you won ${winnings}")
  print(f"you wont on line : ", *winning_lines)#unpack operator , passes the number of lines to after the asterisk
  return winnings - total_bet # will go into negative if no wins so will be subtracted from balance





def main():
  balance = deposit()
  while True :
      print(f" current balance is ${balance}")
      answer  = input("press enter to spin (q to quit)")
      if answer == 'q':
          break
      else : 
          balance += spin(balance)

  print()
  print(f"you left with {balance}")


main()