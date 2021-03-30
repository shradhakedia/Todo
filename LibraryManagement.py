from collections import defaultdict
class Library:
    def __init__(self,_libname,_booklist,_lend_book=defaultdict(lambda: "Not Present")):
        self.libname=_libname
        self.booklist=_booklist
        self.lend_book=_lend_book
    def donatebook(self,dbook):
        if dbook in self.booklist:
            return "Sorry, The book is already available in the library."
        else:
            self.booklist.append(dbook)
            return f"Thank You for donating \'{dbook}\' in the library."
    def lendbook(self,name,lbook):
        if lbook in self.booklist:
            self.booklist.remove(lbook)
            self.lend_book[lbook]=name
            return f"We lend you \'{lbook}\'"
        elif self.lend_book[lbook]!="Not Present":
            return f"Sorry, This book with name \'{lbook}\' is with {self.lend_book[lbook]}"
        else:
            return "This book is not present in our library."
    def returnbook(self,rbook):
        if self.lend_book[rbook]!="Not Present":
            self.booklist.append(rbook)
            self.lend_book[rbook]="Not Present"
            return "Thank you, for returning the book."
        else:
            return "Invalid Choice."
    def __str__(self):
        return f"Welcome to the Library:{self.libname}\nBooks available :\n{self.booklist}"
if __name__=="__main__":
    objlib=Library("Shradha's Library",["Much Ado About Nothing","Revolution 2020"\
    ,"Rich Dad Poor Dad","The Secret","The Secret Principles For Genius"])
    choice="y"
    while choice!="n":
        print('''\t\tEnter 1:To display the book you want to borrow for
                Enter 2:To borrow a book
                Enter 3:To return a book
                Enter 4:To donate a book''')
        ch=input("Enter your choice:")
        try:
            if ch=='1':
                print(objlib)
            elif ch=='2':
                name=input("Enter your name:")
                lbook=input("Enter the book you want to borrow:")
                print(objlib.lendbook(name,lbook.title()))
            elif ch=='3':
                rbook=input("Enter the book name you want to return:")
                print(objlib.returnbook(rbook.title()))
            elif ch=='4':
                dbook=input("Enter the book name you want to donate:")
                print(objlib.donatebook(dbook.title()))
            else:
                print("Invalid choice")
        except Exception as e:
            print(e)
        choice=input("Enter y to continue, n to exit:")