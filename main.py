print('Enter the decimal number: ',end=' ')
number = int(input())
original_number = number
lst = []

# Loop to calculate binary number and quotient
while number > 0:
    lst.append(number%2)
    number = int(number/2)

# Reverse the list
lst.reverse()

print('The binary number of the decimal number: ',end=' ')

# Transfer the lst to string
for i in lst:
    print(i, end=' ')