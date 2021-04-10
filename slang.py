def calculateNGrams(text, n):
    #sizeGrams=len(text)/n
    listaStrings = []
    if(n<=0):
        print("Ngram not possible")
        return 0
    for i in range(0,len(text)-n+1):
        listaStrings.append(text[i : i + n])
    return listaStrings

#Step 2
    
def mostFrequentNGram(text,n):
    ngrams=calculateNGrams(text,n)
    if ngrams==0:
        return "Most frequent ngram not aplicable"
    frequencies = {i:ngrams.count(i) for i in ngrams}
    mostFrequent=0     
    keys=list(frequencies.keys())
    values=list(frequencies.values())
    max_value = max(values)
    max_index = values.index(max_value)
    mostFrequent=keys[max_index] 
    return mostFrequent

