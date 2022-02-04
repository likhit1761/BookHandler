from django.shortcuts import render,redirect
from login.models import BookManager
from booking.models import Booking,Books
from datetime import date
from django.contrib import messages
import datetime

def dashboard(request):
  if not request.session.get('username',None):
      return redirect('manager_login')
  if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
  if request.session.get('username',None) and request.session.get('type',None)=='manager':
      username=request.session['username']
      data=BookManager.objects.get(username=username)
      book_data=data.books_set.all()
      booked=book_data.filter(is_available=False).count()
      print(booked)
      return render(request,"manager_dash/index.html",{"book_data":book_data,"manager":data,"booked":booked})
  else:
      return redirect("manager_login")

def add_book(request):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method=="GET":
        return render(request,"manager_dash/add-book.html",{})
    else:
            book_no=request.POST['book_no']
            book_type=request.POST['book_type']
            price=request.POST['price']
            book_image=request.FILES.get('book_image',None)
            no_of_days_advance=request.POST['no_of_days_advance']
            start_day=request.POST['start_day']
            error=[]
            if(len(book_no)<1):
                error.append(1)
                messages.warning(request,"Book No Field must be atleast 3 digit like 100.")
            if(len(book_type)<5):
                error.append(1)
                messages.warning(request,"Select a valid Book Type.")
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book a book in advance.")
            if(len(start_day)<3):
                error.append(1)
                messages.warning(request,"Please add the starting day")
            if(not len(error)):
                manager=request.session['username']
                manager=BookManager.objects.get(username=manager)
                book=Books(book_no=book_no,book_type=book_type,price=price,no_of_days_advance=no_of_days_advance,start_date=datetime.datetime.strptime(start_day, "%d %B, %Y").date(),book_image=book_image,manager=manager)
                book.save()
                messages.info(request,"Book Added Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-book/new/')

def update_book(request,book_no):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    book=Books.objects.get(book_no=book_no)
    if request.method=="GET":
        return render(request,"manager_dash/edit-book.html",{"book":book})
    else:
            price=request.POST['price']
            no_of_days_advance=request.POST['no_of_days_advance']
            error=[]
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter correct price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book a book in advance.")
            if(not len(error)):
                manager=request.session['username']
                manager=BookManager.objects.get(username=manager)
                book.price=price
                book.no_of_days_advance=no_of_days_advance
                book.save()
                messages.info(request,"Book Data Updated Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-book/update/'+book.book_no,{"book":book})

