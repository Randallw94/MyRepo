# Basic - Print all integers from 0 to 150.
def integers():
    for i in range(151):
        print(i)
    return i

# print(integers())

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def multiples_of_five():
    for i in range(5,1001,5):
        print(i)
    return "Finished calculating multiples of 5"
# print(multiples_of_five())


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def divisible():
    for i in range(1,101):
        if(i % 10 == 0):
            print(i,"- Coding Dojo")
        elif(i % 5 == 0):
            print(i,"Coding")
# print(divisible())

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def totalSum():
    total = 0
    for i in range(0,500001):
        # print(i)
        total += i
# print(f'The total number is:',total)

# Countdown by Fours
# Print positive numbers starting at 2018, counting down by fours.
def countdown():
    for i in range(2018,-1,-4):
        print(i)


# Flexible Counter
# Set three variables: lowNum, highNum, mult. Starting at lowNum and going 
# through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexibleCounter():
    lowNum = 2
    highNum = 9
    mult = 3
    for i in range(lowNum, highNum+1):
        if( i % mult == 0):
            print(i)
print(flexibleCounter())