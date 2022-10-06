word = input()
vowels = ['a', 'e', 'i', 'o', 'u']
vows = 0
cons = 0
for string in word:
    if string in vowels:
        vows += 1
    elif string != ' ':
        cons += 1
print("Vowels : ", vows)
print("Cons : ", cons)
