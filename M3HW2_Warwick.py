# CTI-110
# M3LAB - Software Sales
# Cameron Warwick
# 9/13/17

def main():
    # This program asks the user to ender a number of packages purchased, then displays the amount of the discount and the total purchase cost with the discount applied

    # -Values-
    price = 99
    discount10 = .10
    discount20 = .20
    discount30 = .30
    discount40 = .40

    quantity = int(input('Please enter the amount of packages bought: '))
    total = quantity * price

    if quantity < 10:
        print('Not enough product sold for a discount, sorry!')
        print('The total comes to',total)
        
    elif quantity >= 10 and quantity < 20:
        print('You get a 10% discount!')
        discountTotal1 = total * discount10
        totalSum1 = total - discountTotal1
        print('The total comes to',format(totalSum1,'.2f'))

    elif quantity >= 20 and quantity < 50:
        print('You get a 20% discount!')
        discountTotal2 = total * discount20
        totalSum2 = total - discountTotal2
        print('The total comes to',format(totalSum2,'.2f'))

    elif quantity >= 50 and quantity < 100:
        print('You get a 30% discount!')
        discountTotal3 = total * discount30
        totalSum3 = total - discountTotal3
        print('The total comes to',format(totalSum3,'.2f'))
    else:
        print('You get a 40% discount!')
        discountTotal4 = total * discount40
        totalSum4 = total - discountTotal4
        print('The total comes to',format(totalSum4,'.2f'))
        

# Run
main()
                   
