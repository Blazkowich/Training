words = input("Word? : ")
howmanywords = dict()
dictkey = howmanywords.keys()
for word in words:
    if word in dictkey:
        print(f"{word} - Word is not unical")
    else:
        howmanywords[word] = 1
