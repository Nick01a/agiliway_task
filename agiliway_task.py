def freq(n, text):
    text = ''.join(i.lower() for i in text if i.isdigit() or i.isalpha()) #String preprocessing
    no_dupls = set()                        #set to remove combination dupls
    res_dct = dict()                        #dict with results
    if len(text)==n:                        #specific case (N = text length)
        res_dct[text]=1
    for i in range(len(text)-n):
        no_dupls.add(text[i:i+n])
    for i in no_dupls:
        res_dct[i]=text.count(i)
    return sorted(res_dct.items(), key=lambda x:x[1], reverse=True)       #sort by dict values.


#Tests 
print(freq(1, "abracadabra"))
print(freq(2, "abracadabra"))
print(freq(2, "ab"))
print(freq(2, "abab"))
print(freq(3, "abracadabra"))
print(freq(2, "to be or not to be"))


