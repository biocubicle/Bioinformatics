#Finding the frequency of a base in a half strand from a specific postion in the genome.

#Input - A sequence of the genome and a particular symbol corresponding to a base
#Output - A dictionary which tells us the number of that base in that window at differnt positions in the genome.

#Step I: Use a function to count the number of the base in the genome. This will be similar to the pattern count algorithm that we previously used.
def SymbolCount(Genome,symbol):
    count = 0
    for i in range(len(Genome)-len(symbol)+1):
        if Genome [i:i +len(symbol)] == symbol:
            count = count +1
    return count
#This function will allows us to get the frequency of the base in the genome. But now we need to add another function that will use the genome sequence and the SymbolCount function in the right manner.

#Step II: Define a function to store the frequency and positions for that frequency in an array.
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2] #This line will ensure that the ends of the genome sequence are added again in the sequence to cover all the possible combinations for the window.
    array[0] = SymbolCount(Genome[0:n//2],symbol) #We first define the 0th element of the dictionary and use the count function to get the number of bases in that window
    for i in range (1,n):
        array[i] = array[i-1] #Ask to start be assigning current val being evaluated to the previous val
        if ExtendedGenome [i-1] == symbol: # if the previous window had the base from where we shifted, we need to subtract one from the count as we want to shift the window.
            array[i] = array [i] -1
        if ExtendedGenome [i+n//2-1] == symbol: # if the next window has an element at the new shifted position then add one to the count.
            array [i] = array [i] +1
    return array
# we use two if loops as both the conditions can be TRUE and hence changes need to be made. We only use the counting loop for the first window or 0th element in the dictionary and use its value to make changes according to the frame shift. This shift will only update the count based on the elements
# at the first and last position in the window. If they contain the base, the count will updateded accordingly
#Step III: Take an input from the user.
gen = str(input('Please enter the genome sequence: '))
sym = str(input('Please enter the base that you are trying to search: '))

#Step IV: Call the function and obtain the results.
print(FasterSymbolArray(gen,sym))
