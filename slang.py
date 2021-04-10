#Time complexity= O(n)*O(1)=O(n)
def calculateNGrams(text, n):
    
    listStrings = []
    #Edge case: when n is less or equal to 0
    if(n<=0):
        print("Ngram not possible")
        return 0
    #Iterate over the lenght of the text minus n, so we can have pointers at the beginning until the end of the string
    #Time complexity O(n)
    for i in range(0,len(text)-n+1):
        #it looks for the substring [i:i+n]
        listStrings.append(text[i : i + n]) #T.C=O(1)
    return listStrings

#Step 2
    
#T.C=O(n)*O(m)
def mostFrequentNGram(text,n):
    ngrams=calculateNGrams(text,n)
    #In case the n=0, then we cannot find the most frequent ngram
    if ngrams==0:
        return "Most frequent ngram not aplicable"

    #We count how many times appears each substring in the ngram list and put it in a dict with their respectives frequencies
    frequencies = {i:ngrams.count(i) for i in ngrams} #T.C= O(n)
    mostFrequent=0     
    keys=list(frequencies.keys())
    values=list(frequencies.values())
    #The max function takes the first largest number it finds
    max_value = max(values)  #T.C = O(m)
    #Because we know that the keys and the values share the same index if we put it separately in two lists, then we can find the index of the max value
    max_index = values.index(max_value)
    mostFrequent=keys[max_index] 
    return mostFrequent

