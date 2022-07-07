#Working out the reverse complement of a strand
#Step I: Define a function that will call two other functions and return the processed pattern
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse a string
    Pattern = Complement(Pattern) # complement a string
    return Pattern # return the processed pattern
#Step II: Define a function that will reverse the pattern taken from the user
def Reverse(Pattern): #reverse the pattern
    rev = '' #am empty varibale
    for cnt in reversed (range(len(Pattern))): # reversed () is function which will reverse the order of string elements
        rev = rev + Pattern[cnt] #but this reversed list will need to be stored in the empty varible and each element should be followed by the next in a reverse order and hence (rev = rev + Pattern [cnt])
    return rev
#Step III: Define a function that will process the complement of that reverse
def Complement(Pattern): #figure out the complement
    transf = Pattern.maketrans("ATGC", "TACG") #we define a variable wherein we are calling a function: Pattern.maketrans(). This function requires three parametric inputs ('WHAT NEEDS TO BE CHANGED?','WHAT TO CHANGE IT TO?','WHAT TO DELETE?')
    Pattern = Pattern.translate(transf) #translate() makes the changes according to the inputs we give
    return Pattern

#Another approach for the complement processing can be as follows: 
#def Complement(Pattern):
#    comp = ''
#   for i in range (0, (len(Pattern))):
#        changeChar = 'NA'
#        if Pattern[i] == 'A':
#            changeChar = 'T'
#        elif Pattern[i] == 'C':
#            changeChar = 'G'
#        elif Pattern[i] == 'G':
#            changeChar = 'C'
#        elif Pattern[i] == 'T':
#            changeChar = 'A'
#        comp = comp + changeChar
#    return comp

#Step IV: Get an input from the user
pat = str(input('Please enter a sequence for which the reverse complement needs to be processed: '))
#Step V: Call the function and obtain the processed results
print (ReverseComplement(pat))
