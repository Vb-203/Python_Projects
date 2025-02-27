acronym = input("What is a phrase you would like a acronym for: ")
words = acronym.split()
#print(words)
together = ""
for i in words:
    #print(i[0].upper())
    together = together + i[0].upper()

print(together)



