#Identifying a clump in window L, using a given sequence and k-length.
#Input - The genome in which you want to look for pattern, the length of the pattern you are looking for, a window of length L in which to scan for pattern (per iteration of the algo)
#Output - All the kmers that can be considered as a significant clump

#Step I: We set up a dictionary that will store the patterns identified as keys and their frequency t as that key's value.
def FrequencyMap(Genome, k):
    freq = {}       #An empty dictionary, which will store how many times each seq appears in the genome
    n = len(Genome)
    for i in range(n-k+1):
        Pattern = Genome[i:i+k] #What should be considered a pattern.
        freq[Pattern] = 0 #This will add the keys that were defined by the variable called Pattern we created above and assign all their values to 0
        for j in range(n-k+1): #a second loop is defined as the previous loop focuses on creating all the possible keys and assigning thier frequencies to 0
            if Pattern == Genome[j:j+k]: #if the Pattern (which is now a key in the dictionary) matches with the pattern in the search window
                freq[Pattern] = freq[Pattern] + 1 # add one to the value assocaited with that pattern; intially for all the patterns it will add 1 to 0
    return freq
#Now we have our frequency table ready for each pattern
#Step II: Noting down the clumps that fit into our criteria and have a high frequency
def ClumpFinding(Genome, l, t, k):
    clump = [] #an empty list
    rn = len(Genome) - k + 1
    for i in range(rn):
        seq = Genome[i:i+l]  #define a varible called seq. It defines the window of our clump search
        fremap = FrequencyMap(Genome, k)
        for key in fremap:
            if fremap[key] >= t: #if the frequency of a pattern is greater than or equal to our approved value
                if key not in clump:  #and if that key is not already in the empty list call clump
                    clump.append(key) #add that key to the list
    return clump #return the updated and complete list of clumps
#Step III: Get input from the user
gen = str(input('Please enter the sequence for which you need to identify the clumps: '))
l = int(input('Please enter the window l, in which you want to range your searches: '))
t = int(input('Please enter the acceptable frequency for a pattern, t: '))
k = int(input('Please enter k, the length of the patterns that you are looking for: '))
#Step IV: Call the function and get the output
var = ClumpFinding (gen,l,t,k)
print('Following clumps have been identified: '+ str(var))
