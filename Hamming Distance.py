#Finding the number of mismatches between two strings - i.e. Hammings Distance

#Input - Two genome sequences of equal length with mismatches
#Output- the number of mismatches between the two inputs

#Step I: Define a function to evaluate the number of mismatches
def HammingDistance(p, q):
    cnt = 0
    for char in range (len(p)):
        if p[char] != q[char]:
            cnt =cnt +1
    return cnt

#Step II: Take input from the user
first_in = str(input('Please enter the first sequence: '))
second_in = str(input('Please enter the second sequence: '))

#Step III: Call the function and print the result
print('The Hamming Distance is: '+str(HammingDistance(first_in,second_in)))
