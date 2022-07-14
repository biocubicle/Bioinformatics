#Calculating the entrophy for a given profile matrix
#Input - a set of values for probability
#Output - the entropy for that profile matrix.

from math import log
prof_prob = [.2,.1,.7,.2,.6,.2,1,1,.9,.1,.9,.1,.9,.1,.1,.4,.5,.1,.1,.8,.1,.2,.7,.3,.4,.3,.6,.4]

def entropy(probs):
    entro = 0.
    for i in prof_prob:
        entro -= i * log(i, 2)
    return entro
entropy(prof_prob)
 #We want this vlaue to be as small as possible, as a sequence with this value will be the most conserved in comparison to the consensus sequence
