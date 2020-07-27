def numberToBinary(num):
    """Takes a base10 number and converts to a binary string with 8 bits"""
    binary = ""
    #Convert from decimal to binary
    #Algorithm: divide number by 2 and look at remainder.
    #Add that remainder (0 or 1) to the left side of the binary number
    #Repeat until the number is zero
    #Example:   13 / 2 = 6  remainder 1
    #           6 / 2 = 3   remainder 0
    #           3 / 2 = 1   remainder 1
    #           1 / 2 = 0   remainder 1
    # 13 = 1101 in binary (it was the remainders in reverse order)


    #Make sure it has 8 bits

    return binary

def binaryToNumber(bin):
    """Takes a string binary value and converts it to a base10 integer."""
    decimal = 0
    #Look at the last digit and the base of that spot
    #Add the values as we go

    return decimal

def textToNumbers(text):
    """Takes a string and returns a list of ASCII values."""
    nums =[]

    return nums

def numbersToText(nums):
    """Takes a list of ASCII values and returns a text string."""
    text = ""

    return text

def tests():
    num = 5
    bin = numberToBinary(num)
    print(num, bin)

tests()
