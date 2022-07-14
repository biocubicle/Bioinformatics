#Finding the motif - greedy search approach
    #The approach that was previously mentioned used the Brute Search techinique - chceking for every possible answer and then settling on the most accurate one.
    # But since it is time consuming, now the greedy approach will be employed - which might not result in the most accurate answer for each iteration - it is not too bad!

#Step I: Use probability to identify the if a given kmer is likely to be closer to the consensus seq using a profile matrix.
#Input - a kmer and profile matrix
#Output - a float that will indicate the probability of that kmer to be a transcription binding site relative to a consensus seq.

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i] # Profile[Text[i]][i] refers to the value from the profile for that nucleotide at that position in the given sequence; wherein, Text[i] will give the nucleotide at that index in the sequence
    return p #in the above line, the value of p keeps getting updated as the loop runs through the string and results in the value of probability

#Step II: Identify the most likely kmer from a given string and profile matrix
#Input - a sequence, k, matrix Profile
#Output - a kmer that is most probable based on the given input

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

#****************************************************************************************************************************************************************************************************************************************

#Step III: Combining all that we know in order to find the best possible candidates for the kmers or regualtory motifs.
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    for i in 'ACTG':
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile

def Score(Motifs):
    score = 0
    k = len(Motifs[0])
    cons = Consensus(Motifs)
    for moti in Motifs:
        for location in range(k):
            if moti[location] != cons[location]:
                score += 1
    return score

def Pr(Text, Profile):
    p=1
    k = len(Profile["A"])
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p


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

def GreedyMotifSearch(Dna,k,t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
Dna = [""]
t=len(Dna)
k=
Motifs = GreedyMotifSearch(Dna, k, t)
