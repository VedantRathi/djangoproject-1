from django.shortcuts import render
from Books import forms
from Books import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def userLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('http://localhost:8000/Books/view-books')
        else:
            data['error']='Username or Password is incorrect'
            return render(request,'Books/user_login.html',data)
    else:
        return render(request,'Books/user_login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/Books/user-login')

@login_required(login_url='http://localhost:8000/Books/user-login')
def viewBooks(request):
    books=models.booksTable.objects.all()
    res=render(request,'Books/view_books.html',{'books':books})
    return res

@login_required(login_url='http://localhost:8000/Books/user-login')
def insertBook(request):
    form=forms.newForm()
    res=render(request,'Books/insert_book.html',{'form':form})
    return res

@login_required(login_url='http://localhost:8000/Books/user-login')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.booksTable.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/Books/view-books')

@login_required(login_url='http://localhost:8000/Books/user-login')
def editBook(request):
    book=models.booksTable.objects.get(id=request.GET['bookid'])
    fields={'name':book.name,'author':book.author,'price':book.price,'publisher':book.publisher}
    form=forms.newForm(initial=fields)
    res=render(request,'Books/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url='http://localhost:8000/Books/user-login')
def edit(request):
    if request.method == 'POST':
        form=forms.newForm(request.POST)
        book=models.booksTable()
        book.id=request.POST['bookid']
        book.name=form.data['name']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('http://localhost:8000/Books/view-books')

@login_required(login_url='http://localhost:8000/Books/user-login')
def searchBook(request):
        form=forms.searchForm()
        res=render(request,'Books/search_book.html',{'form':form})
        return res

@login_required(login_url='http://localhost:8000/Books/user-login')
def search(request):
        form=forms.searchForm(request.POST)
        books=models.booksTable.objects.filter(name=request.POST['name'])
        res=render(request,'Books/search_book.html',{'form':form , 'books':books})
        return res

@login_required(login_url='http://localhost:8000/Books/user-login')
def insert(request):
    if request.method=='POST':
        form=forms.newForm(request.POST)
        book=models.booksTable()
        book.name=form.data['name']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisher=form.data['publisher']
        book.save()
    s='Record Inserted Successfully'
    return HttpResponse(s)
