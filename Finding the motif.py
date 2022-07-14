#Finding the motif :
    # Different genes are regulated by regulatory proteins (which in turn are encoded by "clock" genes)
    # These regulatory proteins recognise regulatory motifs or transcription binding sites upstream different genes.
    # These sites have different variations from an optimal sequence (consensus), and to identify this ideal conserved sequence, we carryout this process.
    # From a t number of DNA strings (length n), we select k-mers for each string and form a collection of possible motifs. This collection is then worked on to identify the consensus seq.

# Part I: The count matrix
#Input - a set of kmer motifs stored as a dictionary where i refers to each string and j refers to the columns of the motifs.  
#Output - a dictionary that stores the number of times nucleotide i appears in column j of motifs. 

def Count(Motifs):
    count = {} # an empty dictionary
    k = len(Motifs[0]) # it is the number of symbols in the first string of our motifs dictionary (first row of the dictionary)
    for symbol in "ACGT":
        count[symbol] = [] # we create an empty list in the dicitionary for every symbol: ACGT
        for j in range(k): # j refers to the column# in the matrix and in this case each column of the first row is the range for this loop 
             count[symbol].append(0) # assign the frequency of each symbol present column-wise to 0 (these symbols are the keys of the dictionary)
    t = len(Motifs) # number of motifs (number of strings in the matrix)
    for i in range(t): # for the string in the matrix
        for j in range(k): # for the columns in the first motif
            char = Motifs[i][j] #char is being defined here
            count[char][j] += 1 # add 1 once you encounter a char in a particular column of the matrix
    return count

#Part II: The profile matrix
# Input - a set of kmer motifs stored as a list
# Output - a profile matrix of the set of motifs

def Profile(Motifs):
    profile = {} #empty dictionary
    profile = Count(Motifs) #we assign that dictionary to contain the values of counts using the previously defined count function
    t = len(Motifs) # number of strings
    k = len(Motifs[0]) # number of characters in the first string
    for i in profile:
        for j in range(k):
            profile[i][j] = profile[i][j]/t # an element in profile is equal to that element's value calculated using count divided by the number of string
    return profile

#Part III: Consensus
# Input - a set of kmer motifs stored as a list
# Output - a string that stores the consensus obtained from motifs
def Consensus(Motifs):
    k = len(Motifs[0]) # number of characters in the first string
    count = Count(Motifs) # assign count var and call the Count function
    consensus = "" #empty string variable that will store the consensus
    for j in range(k):
        m = 0
        frequentSymbol = "" #empty string variable
        for symbol in "ACGT":
            if count[symbol][j] > m: # this will iterate till we get the most frequent symbol in the column
                m = count[symbol][j]
                frequentSymbol = symbol # store that frequent symbol in the empty list for each column
        consensus += frequentSymbol # update the consensus variable for the frequent symbol of each column
    return consensus

#Part IV: Score
# Input - a set of kmer motifs stored as a list
# Output- a score for the kmers
def Score(Motifs):
    score = 0
    k = len(Motifs[0]) # number of characters in the first string
    cons = Consensus(Motifs) # assign cons var to store the values of the called function that was previously defined.
    for moti in Motifs: #for every string in motifs
        for location in range(k): # and for every location in the range of the the length of the first sequence
            if moti[location] != cons[location]: # if the symbol in motif at that location does not match the symbol in the consensus at that location, add one to the initialized var score.
                score += 1
    return score #This will sum the frequency of all the mismatched symbols in a column in comparison to the consensus seq.

# We now have a score that will allow us to determine what a consensus seq might look like and. We can also score our matrix based on this consensus. Hence we can narrow down on a matrix which will give the lowest possible score.
