def calculateNGrams(text, n):
    #sizeGrams=len(text)/n
    listaStrings = []
    for i in range(0,len(text)-n+1):
        listaStrings.append(text[i : i + n])
    return listaStrings

