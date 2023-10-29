import datetime
import math
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.db.models import F
from django.http import request
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.shortcuts import redirect
from book.models import Book
from pinjam_buku.views import *

#@login_required(login_url='/login')
from django.db.models import Q

def show_main(request):
    books = Book.objects.all()
    
    search_query = request.GET.get('search', '')
    sort_option = request.GET.get('sort', 'title')

    if sort_option == 'rating':
        books = books.order_by('-rating')
    elif sort_option == 'pages':
        books = books.order_by('num_of_pages')
    else:
        books = books.order_by('title')

    if search_query:
        books = books.filter(title__icontains=search_query)

    rows = math.ceil(len(books) / 3)
    bookdata = []

    for i in range(1, rows + 1):
        bookdata.append(books[(i - 1) * 3: i * 3])

    context = {
        'name': request.user.username,
        'app': 'ReadNow',
        'bookdata': bookdata,
        'search_query': search_query,
        'sort_option': sort_option, 
    }
    return render(request, 'main.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

def book_info(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return render(request, 'not_found.html')

    context = {
        'name': request.user.username,
        'book': book,
    }
    return render(request, 'book_info.html', context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")