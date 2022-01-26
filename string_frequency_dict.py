most_freq(n)'''
def most_freq(x):
    d = dict()
    for key in x:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
string=input("Enter a string:")
print(most_freq(string))

