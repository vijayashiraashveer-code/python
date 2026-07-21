def palind(t):
    return t == t[::-1]


t =(1,2,3,3,2,1,)
print("the tuple is flip flop"if palind(t) else "the tuple is not flip flop")