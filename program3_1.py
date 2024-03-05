### Tiago Gomes - COP 1000 #1284
### program3_1.py

### Pseudocode
### PROMPT the user to enter the desired # of Bananas.
### STORE this value as an integer.
### Use an If-Elif-Else Statement to decide the discounted price.
### CALCULATE the discounted price of bananas in this IF statement.
### CALCULATE the Total Cost of the Bananas by multiplying the discounted price by the # of bananas.
### PRINT the Total Cost in a formatted F-String

def main () :
    ### get desired # of bananas
    numOfBananas = int(input("How many bananas do you wish to buy? "))

    ### calculate discounted price
    if numOfBananas <= 12 :
      costOfBananas = .30
    
    elif numOfBananas >= 12 and numOfBananas < 24:
      costOfBananas = .28
      
    elif numOfBananas >= 24 and numOfBananas < 36:
      costOfBananas = .26
      
    elif numOfBananas >= 36 :
      costOfBananas = .24

    ### calculate total cost
    totalCost = numOfBananas * costOfBananas
    ### print in formatted string
    print(f'Total Cost of the Bananas is ${totalCost:,.2f}')

main ()
