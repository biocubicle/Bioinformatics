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
