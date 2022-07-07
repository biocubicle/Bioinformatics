#Find the positions in the genome where the pattern matches with the sequence at that position/index of the genome

#Input - A pattern to look for in the DNA sequence and the DNA sequence itself
#Output - The positions in the genome sequence where the sequence matches with the pattern.

def PatternMatching(Pattern, Genome):
    positions = [] #create an empty list
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome [i:i +len(Pattern)] == Pattern:
            positions.append(i) #add that position in the empty list that we created
    return positions
#Take input from the user
pat = str(input('Please enter the pattern sequence: '))
ge = str(input('Please enter the DNA sequence: '))
#Call the function and obtain the processed results
print(PatternMatching(pat,ge))

