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

#Step II: Define a function to store the frequency and positions for that frequency in an ind.
def Symbol(Genome, symbol):
    ind = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2] #This line will ensure that the ends of the genome sequence are added again in the sequence to cover all the possible combinations for the window.
    for i in range(n):
        ind[i] = SymbolCount(ExtendedGenome[i:i+(n//2)],symbol) #ith element is equal to the frequency of that symbol in that window
    return ind

#Step III: Take an input from the user.
gen = str(input('Please enter the genome sequence: '))
sym = str(input('Please enter the base that you are trying to search: '))

#Step IV: Call the function and obtain the results.
print(Symbol(gen,sym))
