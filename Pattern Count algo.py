####Finding the frequency of a known pattern (k-mer) in a DNA sequence ####

#Step I: Defining a function to count the frequency of a known K-mer (repeating pattern of a known length associated with the concept of DnaA boxes)in a known DNA/ORIC (origin of replication) sequence
def PatternCount(sequence,pattern): #def allows us to define a function (in this case called PatternCount (with function parameter sequence and pattern - input to the function))
    count = 0 #initilaziation of the counting process (this will keep a record of the number of matches we find eventually)
    for i in range(len(sequence)-len(pattern)+1): # accoding to this statement, for a position i in the sequence from starting position, which is zero in python to (e.g., if an Oric_seq has ten bases and pattern has 3), the endpoint of 8. This is done as from the 8th to the 10th position is the last reading frame of 3-mer; after that, shifting again to the 9th position will not yield a 3-mer sequence, as a result of which we might get an error.
        if sequence [i:i +len(pattern)] == pattern: #following the defined range, this if statement allows us to check if that pattern is present in the sequence
            count = count +1 # every time we find a match, just add to this variable that we previously defined
    return count #So that the updated value as a result of function execution is available for use

#Step II: Take inputs from the user for the sequence
#Take an input sequence from the user
oric_seq = str(input('Please enter the DNA/OriC sequence: '))
k_mer = str(input('Please enter the k-mer sequence: '))

#Step III: Calling the function
freqCount = PatternCount(oric_seq,k_mer)
print ('The frequency of K-mer: '+ str(k_mer)+ ' is '+ str(freqCount)+ ' !')

