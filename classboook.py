class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.=is__borrowed = false

    def return_book(self):
        self.is_borrowed = true
        print(f"you have successfully returned '{self.title}'.")

book1 = book("the hobbit","j.r.r. tolkien")
book2 = book("1984","george orwell")
book3 = book("to kill a mokinbird")