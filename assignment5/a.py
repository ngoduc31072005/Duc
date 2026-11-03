text = "toi toi di di hoc"
words = text.split()
counts={}
for i in words:
    if i in counts:
        counts[i]+=1
    else:
        counts[i] = 1
for words, counts in counts.items():
    print(words,counts)