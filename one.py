class Book:
    def __init__(self,id,title,author,price):
        self.id=id
        self.title=title
        self.author=author
        self.price=price
        self.issue=False
class Library:
    def __init__(self):
        self.collection = dict()
        self.booklist=[]
        self.authorcollection = {}
        self.id=0
    def addBook(self,title:str,author:str,price:int):
        new_Book = Book(self.id,title,author,price)
        self.collection[self.id]=new_Book
        self.booklist.append(title)
        if author not in self.authorcollection:
            self.authorcollection[author]=[title]
        else:
            self.authorcollection[author].extend(title)
        self.id+=1
    def display(self,id):
        print(f"ID : {self.collection[id].id}")
        print(f"Title : {self.collection[id].title}")
        print(f"Author : {self.collection[id].author}")
        print(f"Price : {self.collection[id].price}")
        print(f"Avaiability for Issue : {self.collection[id].issue}")
    def title(self,id):
        print(f"Title : {self.collection[id].title}")
    def countofbooks(self):
        print(f"Total Books : {len(self.collection)}")
    def allBooks(self):
        i=0
        for element in self.booklist:
            print(f"{i} : {element}")
            i+=1
    def issue(self,id):
        if self.collection[id].issue==False:
            print("Issued!")
            self.collection[id].issue=True
        else:
            print("Sorry, Already Issued.")
    def authorlisting(self,author):
        print(self.authorcollection[author])
lib = Library()
while True:
    n=int(input("Choose what you have to do. \n1. Add Book. \n2. Display book info. \n3. List all books of author. \n4. Count Books. \n5. List all books \n6. List title of a book. \n7. Issue a book.    \n8. Exit"))
    
    match n:
        case 1:
            title=input("Enter the title of the Book.")
            author=input("Enter the author of the Book.")
            price=int(input("Enter the price of the Book."))
            lib.addBook(title,author,price)
        case 2:
            id=int(input("Enter the id of the book."))
            lib.display(id)
        case 3:
            author=input("Enter the author name")
            lib.authorlisting(author)
        case 4:
            lib.countofbooks()
        case 5:
            lib.allBooks()
        case 6:
            id=int(input("Enter id of the book"))
            lib.title(id)
        case 7:
            id=int(input("Enter id of the book"))
            lib.issue(id)
        case 8:
            exit(0)
            



        