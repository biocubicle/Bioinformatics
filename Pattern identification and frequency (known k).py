#Finding the frequency of all possible patterns of a known length k in a DNA sequence 

#Input - DNA sequence and the length of the pattern that we are looking for 
#Output - A list of all the possible patterns and their frequency; from which we then print the patterns that appear maximum number of times. 


#Step I: Define a function and assocaited conditions/ loops to obtain a dictionary that resembles a frequency table. This is where we will see all the possible sequence and their assocaited frequencies.
def FrequencyMap(Text, k):
    freq = {} # This is an empty dictionary which in this case will act like a frequency table in which a particular kmer/ pattern is stored in association with its frequency
    n = len(Text) #We compute the length of the sequence, i.e. we work out the number of characters present in this sequence
    for i in range(n-k+1): # i here refers specifically to the positions/ indexes of the sequence that was taken from the user.
#by subtracting k from n, we establish the position of the end of that first pattern and we add 1 to it because, indexing in python starts from 0. As a result of this, we need to account for an additinoal counting index for the number of characters and index to match.
        Pattern = Text[i:i+k] # we are trying to define what a pattern is. For example if we are trying to look for a 3-mer, k=3, a patter is that which starts at 0 and ends at 3. The fact that it ends a three indicates that the last character taken into account was at 2nd position and hence a 3-mer = characters at positions 0,1,2.
        if Pattern in freq: # once this pattern has been identified,
            count = freq[Pattern]
            count = count + 1 #if it is present in the dictionary, and has a frequency of 0, add 1 to it
            freq[Pattern]= count
        else:
            freq[Pattern] = 1 #else, since it is not repeating again, simply add one. This is done because for the pattern to exist in the dictionary in the first place, it needs to occur atleast once.
    return freq

#Step II: Define a function that can identify frequent words of a particular length k from a given sequence
def FrequentWords(Text, k):
    words = [] # This is an empty list in which we will end up storing these frequent words of a particular known length k
    freq = FrequencyMap(Text, k)  #This variable will call a function that has been defined below and use it on the given input (seq and len of k)
    m = max(freq.values()) #We want to get the k-mer with a maximum frequency and hence are using max(). .values() allows us to access the values of the frequencies only instead of the recognised kmers.
    for key in freq:
        if freq[key] == m: #if a key has a maximum frequency,
            words.append(key) #add that key to the list called words
        # add each key to words whose corresponding frequency value is equal to m
    return words

#Step III: Get the input of a sequence and length of k from the user.
dna_seq =str((input('Plese enter the sequence for which you need to identify the kmer: ')))
k_val = int((input('Kindly submit the length of the kmer that you are searching for: ')))
#Step IV: Call onto the predefined function and print the results out!
idnt = FrequencyMap(dna_seq,k_val)
print (idnt)
max_kmers = FrequentWords(dna_seq,k_val)
print ('The most likely k-mer is/are:'+ str(max_kmers))
