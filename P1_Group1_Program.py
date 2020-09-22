#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##sequential Algorithm
def sequential(m, n): #let m & n be the query sequence and the genomes sequence respectively
    print("Running Sequential Algorithm...")
    index = []
    for i in range(len(n) - len(m) + 1): 
        match = True #Assume there is a match
        for j in range(len(m)):
            if n[i+j] != m[j]: #checks if the first index of query matches with genome, if not, match = False. If it is a match, the 2nd index of query checks with next index of genome, carries on until no match found or when m reaches the end.
                match = False  #breaks the inner loop to carry on looping genome sequence
                break
        if match:
          index.append(i) #append the index of the match to a new array 
    return index

def RKS(m, n):
    print("Running RKS Algorithm...")
    dict = {'A':1 , 'C':2, 'G':3,'T':4, }

    pattern = m
    genome = n
    pattern_val= 0
    correct_index = []
    M = len(pattern)
    genome_val= 0
    #to find the hash value of pattern first
    for j in range(M):
        pattern_val += dict[pattern[j]] * (pow(5,j)) #calculate pattern hash value


    for j in range(M):
        genome_val += dict[genome[j]] *(pow(5,j)) #calculate genome hash value
      
    #looping the genome
    for i in range( len(genome) - len(pattern) + 1 ):
        match = False
        #to compare the genome hash value to the pattern
        if genome_val == pattern_val: 
            #now, we simply compare if the string is the same
            for a in range(M):
                if genome[i+a]==pattern[a]:
                    match= True
                    
                else:
                    match = False
                    break
        if match == True :
            correct_index.append(i)

        if i< len(genome)- M:
            genome_val =int((genome_val-dict[genome[i]])/5 )+ dict[genome[i+M]]*(pow(5,M-1))
            
    return correct_index

def KMP(m, n):
    print("Running KMP Algorithm...")

    ##giving them a name
    query = m
    genome = n

    queryKMP = []
    queryKMP.append(0)
    i = 0

    #pre-processing:
    for j in range(1, len(query)):
        if query[i] == query[j]:
            queryKMP.append(i+1)
            i+=1
        else:
            while(query[i]!=query[j] and i != 0):
                i-=1
            queryKMP.append(i)
    print(queryKMP)

    #search
    index = []
    current = 0
    for i in range(len(genome) - len(query) + 1):
        match = True #Assume there is a match
        for j in range(len(query)):
            if ((j + current) < len(query)):
                j += current
            if genome[i+j] != query[j]:
                current=queryKMP[j-1]
                match = False
                break
        if match:
            index.append(i)
            current = 0
        i+=current
    return index

def main():
    while(1):
        ##read genome file 
        n = open("GCA_000859985.2_ViralProj15217_genomic.fna", "r")     
        #next(n)  
        n = n.read().replace("\n","") #remove all new line
        n = n[58:] #remove the header words
        
        print("Choose Algorithm method:")
        print("Enter 1 for Sequential Search")
        print("Enter 2 for Knuth–Morris–Pratt Algorithm")
        print("Enter 3 for Rabin-Karp String Matching Algorithm")
            
        try:
            choice = int(input())
            querySequence = input("Input your query, must be A T G C only.") #query sequence

            if choice == 1:
                index = sequential(querySequence, n)
            elif choice == 2:
                index = KMP(querySequence, n)
            elif choice == 3:
                index = RKS(querySequence, n)
            else :
                print("Please enter 1 or 2 or 3")
            # if query sequence is not found in the genome   
            if index==[]:
                print("The sequence is not found in the Genome (no occurence).")
            else:
                print("The location of the sequence is at:\n", index)        
        except:
            print("Please enter the given number & values!\n")
        
    
main()


# In[ ]:





# In[ ]:





# In[ ]:




