# CTI-110 
# M2HW2 - Tip Tax Total 
# Cameron Warwick
# 9/6/17

foodCost = int(input('Please input the cost of the meal: '))
tipAmount = .18 * foodCost
salesTax = .07 * foodCost
totalCost = foodCost + tipAmount + salesTax
print ('Food cost: ',foodCost)
print ('Tip amount: ',tipAmount)
print ('Sales tax: ',salesTax)
print ('Total cost: ',totalCost)
