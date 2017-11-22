# CTI-110
# M5HW2 - Running Total
# Cameron Warwick
# 10/30/17

def main():
    runningTotal = 0
    add= 0
    keepGoing = 1
    while keepGoing > 0:
        add = int(input('Please enter the number you would like to add to the total: '))
        if add >= 0 :
            runningTotal = runningTotal + add
            print('Current total:',runningTotal)
        else:
            keepGoing = 0
            print('The final count is',runningTotal)
        
main()
        
        
        
    
    
