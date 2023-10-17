print(".......Library Management System..........")
username = "ANUSHREE"
password = 7225
available_books = {"maths" : 4, "hindi" : 2 , "chem" : 5}
borrowed_books = {}

while True:
    input_username = input("Enter Username: ")
    input_password = int(input("Enter Password: "))
    if input_username == username and input_password == password:
        print("Login Successfully.....")
        break
    else:
        print("Please enter valid username and password......")

while True:
    print("Library Management System Menu.....")
    print("1. Total Books available")
    print("2. Borrow books")
    print("3. return books")
    print("4: borrowed books details")
    print("5. Increase books count")
    print("6: Descrease book count")
    print("7. Exit")

    choice = input("ENTER YOUR CHOICE: ")
    if choice == "1":
        print("Total books available: ",available_books.items())

    elif choice == "2":
        book_name = input("Enter the book name: ") 
        borrower_name = input("Enter your name: ")
        if book_name in available_books:
            available_books[book_name]-= 1  
            borrowed_books[borrower_name] = book_name
            print(f"{book_name} was successfully borrowed by {borrower_name} ")

    elif choice == "3":
        borrower_name = input("enter yuor name")  
        if borrower_name in borrowed_books:
            return_books = borrowed_books.pop(book_name) 
            available_books[book_name]+=1
            print(f"{return_books} returned by {book_name}") 

        else:
            print("You have no borrowed any book....")   


    elif choice == "4":
        print(borrowed_books.items())


    elif choice == "5":
        book_name = input("Enter the book name you want to increase: ")  
        quantity = int(input("enter the quantity you want to increase: "))
        if book_name in available_books:
            available_books[book_name]+= quantity
            print(f"{book_name} was increased by {quantity}")
        else:
            print("Book not available...")  


    elif choice == "6":
        book_name = input("Enter the book name you want to descrease: ")  
        quantity = int(input("enter the quantity you want to descrease: "))
        if book_name in available_books:
            available_books[book_name]+= quantity
            print(f"{book_name} was descrese by {quantity}")
        else:
            print("Book not available..")  

    
    elif choice == "7":
        print("Thankyou for using Library Management System....,Good By")
        break
    else:
        print("INVALID CHOICE")
