# Library Management System
Project Live: https://library--managementsystem.herokuapp.com/

# Overview

### Book Dashboard
* The Book dashboard displays all the book record that are available in the database.Dashborad also display the **Total no. of book, Book stock and Rented book to member**.
* User can perform operations of **AddBook,ImportBook,Search,Edit,Delete** and **RentBookToMember** .
    * **AddBook:** Click Add Book button then fill the form and submit. 
    * **ImportBook:** Click Import Book button then pass the keyword for single and multiple search and can also pass quantity for individual book. To get the random book record then just click the submit button without filling any field.
    * **Search:** Search keyword for Title and Author.
    * **Edit:** Click edit button to edit the book record like title,author,publisher,isbn and quantity of the book.
    * **Delete:** Click delete button to delete the book record and if book is rented to the member then book record will not delete.
    * **RentBookToMember:** Click Rent To button and then it will navigate to the member dashboard and then select the member to rent the book.

#### Book Dashboard
![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/Book.png)

#### Book Import
![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/BookImport.png)

#### Delete Book
* If the book is rented to the member then book record will not delete and show warning massage.

![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/BookDelete.png)

#### Rent Book
* Click Rent To button from book dashboard then it will navigate to this page and then select the member and the trasaction record will display in transaction dashboard.

![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/BookRentto.png)

### Member Dashboard
* The Member dashboard displays all the member record that are available in the database.Dashboard also display the **Balance and Debt** of the member.

![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/Member.png)

#### Add Member
![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/MemberAdd.png)

#### Delete Member
* If the book is rented to the member then member record will not delete and show warning massage.

![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/MemberDelete.png)

### Transaction Dashboard
* The Member dashboard displays all the transactions record of member and book. It also display  **borrowed date ,returned date and the amount to be paid**.
* if member wants to return the book then click the return button and it will calculate and show returned date ,total days, total charge and Amount paid. 
* Amount paid is calculate from the balance of the member and if balance is not enough the it will add to the debt of the member.
* The fees for renting book is 10/day i.e.  **otal_days *10 **.

![404 Image Not Found](https://github.com/bobbyvish/Library_Management_system/blob/master/images/Transactions.png)

---

## To Install:

Cloning the Repository:

```
$ git clone https://github.com/bobbyvish/Library_Management_system.git

$ cd Library_Management_system 

```

Installing the environment control:

```
$ pip install virtualenv

$ virtualenv env

```

Activating the environment:

on Windows:
```
env\Scripts\activate

```
on Mac OS / Linux:
```
$ source env/bin/activate

```

Installing dependencies:

```
$ pip install -r requirements.txt

```

Copy and rename the file of env.example as .env and then setting all requirements without using space after "=".

```
DJANGO_DEBUG=
SECRET_KEY=
DB_DATABASE=
DB_HOST=
DB_USERNAME=root
DB_PASSWORD=
DB_PORT=3306

```

Last commands to start:

```
$ python manage.py makemigrations

$ python manage.py migrate

```

Finishing running server:

```
$ python manage.py runserver

```

### Thank you!!
