# Finding the (total number of G) - (total number of C) inorder to understand the skew of the genome to locate the oriC

#Input - genome sequence
#Output - an array with the difference between total G and C numbers

#Step I: Define a function
def Skew(Genome):
    Skew = {} #empty dictionary
    n = len(Genome)
    Skew[0] = 0 #assign the first element to be 0 in the dictionary {0:0 1:Val for G-C....}
    for i in range(n): #the range of this loop has been defined according to the indexing of Genome and not Skew
        if Genome[i] == "C":
            Skew[i+1] = Skew[i] - 1 # After looking at the range that has been defined, a sequence that starts with C, this will be 0-1 since the first element of skew at index 0 has been defined as 0. 0-1=-1
        elif Genome[i] == "G":
            Skew[i+1] = Skew[i] + 1 # If our sequence is CG, then for G, which is at index 1, -1+1 = 0 and hence so far in the sequence, totalG- totalC = 0. No skew so far!
        else:
            Skew[i+1] = Skew[i] # This will retain the value of the previous element and will be applicable for any A/T. This ensures that our totalG - totalC will not change due to A/T.
    return Skew.values()

#Skew II: Call the function and obtain the results.
seq = str(input('Please enter the sequence for which G-C needs to be worked out: '))
print(Skew(seq))
