def printDuplicates(str):
    count = {}
    for i in range(len(str)):
        if str[i] in count:
            count[str[i]] += 1
        else :
            count[str[i]] = 1
    
    for j in count.keys():  #iterating through the unordered map
        if (count[j] > 1):   #if the count of characters is greater than 1 then duplicate found
            print("duplicate value :", j )

Str = "test string"
printDuplicates(Str)