# CTI-110
# M6T1 - Kilometer Converter
# Cameron Warwick
# 10/25/17

def main():
    print("Cameron's Kilometer Converter 2000:")
    km = int(input('Please enter a distance in Kilometers: '))
    showMiles(km)

def showMiles(km):
    mi = km * 0.6214
    print(mi)

    
main()
    
    
