a = input("Enter a text:")
def word_frequency(a):
    s ={}
    words=a.lower().split()
    for i in words:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    return s
print("The frequency of words:", word_frequency(a))