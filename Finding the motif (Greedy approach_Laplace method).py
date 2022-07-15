#Modifying the Greedy Search approach to prevent the elimination of a possible kmer only due to one mismatch with the consensus (due to which the kmers probability equated to zero and results in its elimination).
    #Cromwell's rule states that we should not equate the probability of an event to 0 ot 1 unless it is a logical statement.
    #To improve the scoring, the 0's can be substituted with small numbers known as pseudocounts.
    #These pseudocounts are introduced using Laplace's rule of succession. (+1 to each element of Count(Motifs))

#Step I: Building a count matrix that will account for pseudocounts
#Input - A set of kmers
#Output - Dictionary with pseudocounts
def CountWithPseudocounts(Motifs):
    k = len(Motifs[0])
    count ={} #empty dictionary
    for char in "ACGT":
        count[char] = []
        for j in range(k):
            count[char].append(1) #this will by default make every value for every character at each position one
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j]+=1
    return count

#Step II: Building a profile matrix that will account for the new count matrix
#Input - A set of kmers
#Output - Dictionary of frequencies after normalization
def ProfileWithPseudocounts(Motifs):
    profile = {}
    profile = CountWithPseudocounts(Motifs) # it fills tha empty dictionary with pseudocount values
    t = len(Motifs) + 4 #we add this four to normalize the final profile values (since we addded 1 to each position of each column) #Hint: we want the sum of each column frequencies to equate to 1 not 4 and hence we normalize.
    k = len(Motifs[0])
    for i in profile:
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile

#Step III: Modifying the GreedySearch to use pseudocounts
#Input - DNA input strings (Dna), kmer length (k) and number of DNA strings (t)
#Output - A list of possible kmers for each string
def GreedyMotifSearchWithPseudocounts(Dna,k,t):
    BestMotifs = [] #empty list
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def ProfileWithPseudocounts(Motifs):
    profile = {}
    profile = CountWithPseudocounts(Motifs) # it fills tha empty dictionary with pseudocount values
    t = len(Motifs) + 4 #we add this four to normalize the final profile values (since we addded 1 to each position of each column) #Hint: we want the sum of each column frequencies to equate to 1 not 4 and hence we normalize.
    k = len(Motifs[0])
    for i in profile:
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile

def Score(Motifs):
    consensus = Consensus(Motifs)
    count = CountWithPseudocounts(Motifs)
    k = len(Motifs[0])
    t = len(Motifs)
    cnt = 0
    for Motif in Motifs:
        for i in range(k):
                if Motif[i] != consensus[i]:
                    cnt = cnt+1
    return cnt


def Consensus(Motifs):
    consensus = ""
    k = len(Motifs[0])
    t = len(Motifs)
    count = CountWithPseudocounts(Motifs)
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def CountWithPseudocounts(Motifs):
    k = len(Motifs[0])
    count ={} #empty dictionary
    for char in "ACGT":
        count[char] = []
        for j in range(k):
            count[char].append(1) #this will by default make every value for every character at each position one
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j]+=1
    return count

def ProfileMostProbableKmer(Text, k, Profile):
    prob_cnt = 0
    frequent = Text[:k] #we are tring to define the length of a kmer if it has to be a part of this variable
    n = len(Text)
    for i in range(n-k +1):
        kmer = Text[i:i+k] #what is a kmer?
        probability = Pr(kmer, Profile) #calling the previously defined probability function
        if probability > prob_cnt: #if this probability is greater than 0/the previously calculated probability
            prob_cnt = probability #keep updating the value of this cnt to find the kmer with the highest probability
            frequent = kmer #include this kmer in the variable
    return frequent

def Pr(Text, Profile):

    p = 1
    for i in range(len(Text)):

        p1 = Profile[(Text[i])][i]
        p = p*p1

    return p
#This will result in a better Subtle Motif recognition.
