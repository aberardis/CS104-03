#Sum/Average Program
#Your first and last number: Anthony Berardis
#Your student ID:1297598

#Build on what you did in the 'List of numbers' program
#Instead of entering 10 numbers, enter 20 numbers (integers)
#Instead of searching for a number in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:
total = 0
numList= []
for x in range(0,20):
    number = int(input("Enter a number: "))
    numList.append(number)
 
for x in range(0,20):
    total = total + numList[x]
print("The sum of your twenty numbers is: ", total)
print("The average of your twenty numbers is: ", (total/len(numList)))


