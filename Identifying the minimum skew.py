#Finding the locations in the genome where the skew is minimum inorder to get an estimate for the OriC

#Input - Genome Sequence
#Output - The positions where the skew is minimum

#Step I: Defining a function to identify the minimum skew positions
def MinimumSkew(Genome):
    positions = [] # empty list
    array = Skew(Genome)
    minarray = min(array.values())
    for i in array:
        if array[i] == minarray:
            positions.append(i)
    return positions

#Step II: Defining a function to calcualte the skew
def Skew(Genome):
    k = {} #empty dictionary
    n = len(Genome)
    k[0] = 0 #assign the first element to be 0 in the dictionary {0:0 1:Val for G-C....}
    for i in range(n): #the range of this loop has been defined according to the indexing of Genome and not k
        if Genome[i] == "C":
            k[i+1] = k[i] - 1 # After looking at the range that has been defined, a sequence that starts with C, this will be 0-1 since the first element of skew at index 0 has been defined as 0. 0-1=-1
        elif Genome[i] == "G":
            k[i+1] = k[i] + 1 # If our sequence is CG, then for G, which is at index 1, -1+1 = 0 and hence so far in the sequence, totalG- totalC = 0. No skew so far!
        else:
            k[i+1] = k[i] # This will retain the value of the previous element and will be applicable for any A/T. This ensures that our totalG - totalC will not change due to A/T.
    return k

#Skew II: Call the function and obtain the results.
seq = str(input('Please enter the sequence for which minimum skew positions need to be evaluated: '))
print(MinimumSkew(seq))
