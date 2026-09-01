class myclass :
    __privatevar = 27 
    def__privmeth(self):
        print("i'm inside class myclass")
    def hello(self):
        print("private variable value: ",myclass.__privatevar)
foo = myclass()
foo.hello()
foo.__privmeth
