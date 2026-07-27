i = ["pencil", "eraser", "notebook", "sharpener", "glue"]
d = dict(zip(i,[12,0,8,5,3]0))
x = input("item:")
if x not in d or d[x] == 0:
    print("out")
    exit()
p = list(map(lambda n:n + int(input("markup:")),[10,5,40,15,20]))