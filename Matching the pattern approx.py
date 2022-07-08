#Finding the positions in the genomw where the given pattern matches approximately if not exactly

#Input - a genome sequence, a pattern and the number of mistmatches that are acceptable (denoted by d)
#Output - positions where the patterns match approximately

#Step I: Define a function that will be similar to the pattern matching one previously defined; but with the constraints of d
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] #empty list
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions

# Step II:Use the HammingDistance function
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

#Take input from the user
first_in = str(input('Please enter the genome sequence: '))
second_in = str(input('Please enter the pattern sequence: '))
d_val = int(input('Please enter the acceptable value for Hamming Distance: '))

#Call the function and print the results
print('For the given sequences and HammingDistance, the following positions in the genome have a match for the pattern: '+str(ApproximatePatternMatching(first_in,second_in,d_val)))

