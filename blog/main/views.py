from django.shortcuts import render
import datetime

def main(request):
    '''
    Render the main pages
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很讚','now':now} 
    return render(request,'main/main.html',context)

def about(request):
    '''
    Render the about pages
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很讚','now':now} 
    return render(request,'main/about.html',context)

def book(request):
    '''
    Render the book pages
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很讚','now':now} 
    return render(request,'main/book.html',context)

