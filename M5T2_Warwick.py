# CTI-110
# M5LAB - Bug Collecting
# Cameron Warwick
# 10/9/17

def main():
    totalBugs = 0
    week = range(1,8)
    for day in week:
        todaysBugs = int(input('Please give number of bugs collected today: '))
        totalBugs = todaysBugs + totalBugs
        if day < 7:
            print('Bugs so far: ',totalBugs)
    print('Final count: ',totalBugs)

main()
        
    
        
        
    
