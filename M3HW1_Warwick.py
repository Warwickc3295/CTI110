# CTI-110 
# M3HW1 - Age Classifier 
# Cameron Warwick
# 9/13/17

def main():
    # This program displays a message indicating whether a person is an infant, a child, a teenager, or an adult.

    # -Values-
    child = 1
    teenager = 13
    adult = 20

    age = int(input('Please input your age: '))

    if age <= child:
        print('You are an infant! How are you even using this computer?')
    elif age > child and age < teenager:
        print('You are a child.')
    elif age > teenager and age < adult:
        print('You are a teenager.')
    else:
        print('You are an adult.')

# Run
main()
    
    

