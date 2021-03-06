# Bioinformatics
It contains all the python scripts associated with basic sequence counting and manipulation! 


Pattern Count: #Finding the frequency of a known pattern (k-mer) in a DNA sequence 
#Input - DNA and pattern sequence 
#Output - The frequency of that pattern in the DNA sequence provided

Pattern Identification and frequency: #Finding the frequency of all possible patterns of a known length k in a DNA sequence 
#Input - DNA sequence and the length of the pattern that we are looking for 
#Output - A list of all the possible patterns and their frequency; from which we then print the patterns that appear maximum number of times. 


Working out the reverse complement: #Working out the reverse complement of a strand
#Input - Sequence of a strand 
#Output - The reverse complement of that strand


Pattern Matching: #Find the positions in the genome where the pattern matches with the sequence at that position/index of the genome
#Input - A pattern to look for in the DNA sequence and the DNA sequence itself
#Output - The positions in the genome sequence where the sequence matches with the pattern.


Symbol  - Slow(running time): #Finding the frequency of a base in a half strand from a specific postion in the genome.
#Input - A sequence of the genome and a particular symbol corresponding to a base
#Output - A dictionary which tells us the number of that base in that window at differnt positions in the genome.


Symbol  - Faster(running time): #Finding the frequency of a base in a half strand from a specific postion in the genome.
#Input - A sequence of the genome and a particular symbol corresponding to a base
#Output - A dictionary which tells us the number of that base in that window at differnt positions in the genome.


Skew calculations: # Finding the (total number of G) - (total number of C) inorder to understand the skew of the genome to locate the oriC
#Input - genome sequence
#Output - an array with the difference between total G and C numbers


Identifying the minimum skew positions: #Finding the locations in the genome where the skew is minimum inorder to get an estimate for the OriC
#Input - Genome Sequence
#Output - The positions where the skew is minimum


Hammings Distance: #Finding the number of mismatches between two strings - i.e. Hammings Distance
#Input - Two genome sequences of equal length with mismatches
#Output- the number of mismatches between the two inputs


Matching the pattern approx: #Finding the positions in the genomw where the given pattern matches approximately if not exactly
#Input - a genome sequence, a pattern and the number of mistmatches that are acceptable (denoted by d)
#Output - positions where the patterns match approximately


Finding the motif: #Finding the motif
#Input - kmers / (A set of DNA strings with a value of k) 
#Output - different matrices that aid in identifying a consensus sequence and allows us to score different kmers based on similarity. 


Finding the motif - greedy search approach: #Finding the motif - greedy search approach
#The approach that was previously mentioned used the Brute Search techinique - chceking for every possible answer and then settling on the most accurate one. # But since it is time consuming, now the greedy approach will be employed - which might not result in the most accurate answer for each iteration - it is not too bad! 


Entrpy calculation: #Calculating the entrophy for a given profile matrix
#Input - a set of values for probability
#Output - the entropy for that profile matrix.


#Modifying the Greedy Search approach to prevent the elimination of a possible kmer only due to one mismatch with the consensus (due to which the kmers probability equated to zero and results in its elimination).
    #Cromwell's rule states that we should not equate the probability of an event to 0 ot 1 unless it is a logical statement.
    #To improve the scoring, the 0's can be substituted with small numbers known as pseudocounts.
    #These pseudocounts are introduced using Laplace's rule of succession. (+1 to each element of Count(Motifs))


Clump_finding algo: #Identifying a clump in window L, using a given sequence and k-length.
#Input - The genome in which you want to look for pattern, the length of the pattern you are looking for, a window of length L in which to scan for pattern (per iteration of the algo)
#Output - All the kmers that can be considered as a significant clump
