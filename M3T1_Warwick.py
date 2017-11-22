# CTI-110 
# M3T1 - Areas of Rectangles 
# Cameron Warwick
# 9/11/17

print ('This program is for comparing the sizes of two rectangles!')

rectLength1 = int(input('Please input the length of the first rectangle: '))
rectWidth1 = int(input('Input the width of the first rectangle: '))

rectLength2 = int(input('Now input the length of the second rectangle: '))
rectWidth2 = int(input('finally input the width of the second rectangle: '))

rectArea1 = rectLength1 * rectWidth1
rectArea2 = rectLength2 * rectWidth2

if rectArea1 > rectArea2:
    print('The first rectangle is larger than the second!')
elif rectArea1 == rectArea2:
    print('The rectangles are equal in size')
else:
    print('The second rectangle is larger than the first!')

