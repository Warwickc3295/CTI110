# CTI-110
# M5HW1 - Distance Traveled
# Cameron Warwick
# 10/16/17

def main():
    speed = int(input('Please enter the speed at which the vehicle travles: '))
    time = int(input('Now enter the time it took to travel: '))
    totalDist = 0
    totalTime = 0

    distance = speed * time
    
    

    print('Hour      Distance Traveled')
    print('---------------------------')

    while totalTime < time :
            totalDist = totalDist + distance
            totalTime = totalTime + 1
            print(totalTime,'       ', totalDist)


main()
    

    
    

    
    
    
