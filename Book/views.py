import re
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .forms import BookForm
from .models import Book, Transaction
from Member.models import Member
from django.contrib import messages
import requests
import random
from django.db.models import Q
from Member.models import Member
import datetime

# Funtion for API calling
def API_call(request, *args, **kwargs):
    title=kwargs['title']
    authors=kwargs['author']
    publisher=kwargs['publisher']
    isbn=kwargs['isbn']
    
    BASE_URL='https://frappe.io/api/method/frappe-library?'

    # check if any field is passed then pass parameter of that field
    if title or authors or publisher or isbn:
        query=f'title={title}&authors={authors}&publisher={publisher}&isbn={isbn}'
        response=requests.get(BASE_URL+query).json()['message']
    
    else:
        #fetching data in bulk from random pages
        query=f'page={random.randint(1,100)}'
        response=requests.get(BASE_URL+query).json()['message']

    return response



class BookAddView(View):
    template_name ="book.html"
    context={}

    def get(self, request):
        form=BookForm()
       
        #checking get method for search and search button name=searchdata
        #if search is not pass then show all record
        if 'searchdata' in request.GET:
            search=request.GET.get('search')
            print(search)
            books=Book.objects.filter(Q(title__icontains=search)
                                        | Q(author__icontains=search))
        else:
            books=Book.objects.all() # fetching record from database to show
        
        #passing form, member and url in context
        self.context.update(
            {
            'title': 'Book',
            'form':form,
            'books':books,
            'url' : reverse('books')
            })
        
        return render(request,self.template_name, self.context)

    def post(self, request):
        
        form=BookForm(request.POST)
        #using same form with different submit button name attritube to differentiate 
        # for add book form and import book form
        # add custom book form login
        if 'addcustombook' in request.POST:

            #making form field require true 
            form.fields['title'].required=True
            form.fields['author'].required=True
            form.fields['publisher'].required=True
            form.fields['isbn'].required=True
            if not form.is_valid():
                self.context.update(
                {
                'title' :'Add Book',
                'form':form}
                )
                messages.warning(request,"Some fields are missing,Please fill!")
                return render(request,self.template_name,self.context)

            book=form.save(commit=False)

            #updating book_stock instance through quantity field to show the stock of book
            book.book_stock=book.quantity or 1
            book.save()

            messages.success(request,"Book is successfully added")

        # import book form login
        elif 'importbook' in request.POST:
            if not form.is_valid():
                self.context.update(
                {
                'title' :'Import Book',
                'form':form}
                )
                messages.warning(request,form.errors)
                return render(request,self.template_name,self.context)

            # cleaning all form fields
            title=form.cleaned_data['title']
            author=form.cleaned_data['author']
            publisher=form.cleaned_data['publisher']
            isbn=form.cleaned_data['isbn']
            quantity=form.cleaned_data['quantity']

            # setting kwargs to pass in api_call funtion
            kwargs={
                'title': title,
                'author': author,
                'publisher': publisher,
                'isbn': isbn
            }

            #calling API_call funtion
            api_response =API_call(request, **kwargs)
            #looping through the response and creating a record in database
            for data in api_response:
                
                book_check = Book.objects.filter(title=data['title']).exists()
               
                if book_check == False:
                    book=Book(
                        title=data["title"],
                        author=data["authors"],
                        publisher=data["publisher"],
                        isbn=data["isbn"],
                        quantity=quantity or 1,
                        book_stock=quantity or 1,
                        rented=0
                    )
                    book.save()
                else:
                    pass
            messages.success(request,"Imported Book Successfully")

        return redirect(reverse("books"))

#Book Edit View
class BookEditView(View):
    template_name ="update_form.html"
    context={'title': 'Update Book'}

    def get(self, request, id):
        
        try:
            book_id = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            messages.warning(request, "Book record does not exist")
            return render(request, self.template_name)
        
        form = BookForm(instance=book_id)

        self.context.update({
            'url': reverse('bookedit', kwargs={'id': id}),
            'book_id': book_id,
            'form':form
        })

        return render(request,self.template_name, self.context)
    
    def post(self, request, id):
        try:
            book_id = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            messages.warning(request, "Book record does not exist")
            return render(request, self.template_name)
        
        form = BookForm(request.POST, instance=book_id)
        if not form.is_valid():
            self.context.update(
                            {
                            'form':form
                            })
            return render(request,self.template_name,self.context)
        book=form.save(commit=False)
        #login to update book stock if book quantity is add in store
        book.book_stock=int(book.quantity) - book.rented
        book.save()
        messages.success(request,"Book Record is successfully updated")
        return redirect(reverse("books"))

#Book Delete View
class BookDeleteView(View):
    def get(self, request, id):

        try:
            book_id = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            messages.error(request, "Book record does not exist")
            return redirect(reverse("books"))

        #if book is rented does not delete book record
        if book_id.rented >0:
            messages.warning(request, "Book is rented so record can't be deleted")
            return redirect(reverse("books"))

        book_id.delete()
        messages.success(request, "Book record deleted successfully")
        return redirect(reverse("books"))

#Book rented to member view
class BookRentToView(View):
    template_name = 'rent_to.html'
    context={}
    def get(self, request, id):

        #checking get method for search and search button name=searchdata
        #if search is not pass then show all record
        if 'searchdata' in request.GET:
            search=request.GET.get('search')
            print(search)
            members=Member.objects.filter(Q(member_name__icontains=search)
                                        | Q(member_email__icontains=search))
        
        else:
            members=Member.objects.all()


        book=Book.objects.filter(pk=id).first()

        #login to check if book is in stock before giving to member
        #if book is not in stock just stop the process
        if int(book.book_stock) <=0:
            messages.warning(request,"Book is not in stock!")
            return redirect(reverse('books'))
        
        self.context.update({
            'members': members,
            'url': reverse('bookrentto',kwargs={'id':id})
        })
        return render(request, self.template_name, self.context)
    
    #post for selecting member to rent the book from
    #getting 2 ids 1 from url i.e book_id and 1 from table records thrpugh select button
    def post(self, request, id):

        member_id=request.POST.get('memberId')
        
        #filtering record of member
        member=Member.objects.filter(id=member_id).first()
        #filter record of book to update book stock , quantity and rent
        book=Book.objects.filter(pk=id).first()
        if book:
            book.rented +=1
            book.book_stock=int(book.quantity) - book.rented
            book.save()
        
        #login to check debt is less than 500 if not then does not assign book to member 
        if int(member.debt) < -500:
            messages.warning(request,'You reached to your debt limit, Please Pay!')
            return redirect(reverse('books'))

        # if all logic is ok then create a transaction record in database
        Transaction.objects.create(
            member=member,
            book=book,  
        )

        return redirect(reverse('books'))

class TransactionView(View):
    template_name = 'transaction.html'
    context={}

    def get(self, request):
        #checking get method for search from search button attr name=searchdata
        #if search is not pass then show all record
        if 'searchdata' in request.GET:
            search=request.GET.get('search')
            
            transaction=Transaction.objects.filter(Q(member__member_name__icontains=search)
                                        | Q(book__title__icontains=search))

        else:
            transaction =Transaction.objects.all()
        self.context.update({
            'transactions': transaction,
            'url':reverse('transaction')
        })

        return render(request,self.template_name, self.context)


#return book view if member return book back than update transaction record
class ReturnView(View):
    template_name = 'transaction.html'

    def get(self, request, id):

        try:
            transaction =Transaction.objects.get(pk=id)
        except Transaction.DoesNotExist:
            messages.warning(request,"Transaction Does not exist")
            return render(request,self.template_name)
        
        #updating transaction record if memeber returned book
        transaction.return_date=datetime.date.today()
        transaction.total_days =transaction.calculate_total_days()
        transaction.total_charge =transaction.calculate_total_charge()
        transaction.amount_paid =transaction.calculate_amount_paid()
        transaction.member.balance=float(transaction.member.balance) - float(transaction.amount_paid)
        transaction.save()
        
        member=Member.objects.get(pk=transaction.member.id)
        
        #logic to update member balance and debt after returning book 
        if int(member.balance)>0:
            member.balance=float(member.balance)-float(transaction.amount_paid)
            if member.balance< 0:
                member.debt =float(member.debt) + abs(float(member.balance))
                member.balance=0.00
        else:
            member.debt=abs(float(member.debt)+float(transaction.amount_paid))

        member.save()

        book=Book.objects.get(pk=transaction.book.id)
        #book stock update after member returns book
        if transaction.book.id==book.id and int(transaction.amount_paid)>0:
            
            book.rented -=1
            book.book_stock=int(book.quantity) - book.rented
            book.save()

        return redirect(reverse("transaction"))







