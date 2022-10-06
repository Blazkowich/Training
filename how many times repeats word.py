words = input("Word? : ")
howmanywords = dict()
count = 0
dictkey = howmanywords.keys()
for word in words:
    count += 1
    if word in dictkey:
        howmanywords[word] += 1
    else:
        howmanywords[word] = 1
print(howmanywords)
