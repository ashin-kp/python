class publisher:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"publisher:{self.name}")
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print(f"Title:{self.title}\t Author:{self.author} ")
        super().display()
class Python(book):
    def __init__(self, name, title, author,price,page_no):
        super().__init__(name, title, author)
        self.price=price
        self.page_no=page_no

    def display(self):
       print(f" Price:{self.price}\t Page_no:{self.page_no}")
       super().display()
b=Python('abc','lmoo','ahin',777,5)
b.display()