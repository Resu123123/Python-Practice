from itertools import groupby

for k, c in groupby(input()):
        
    #printing the output
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')