from django.shortcuts import render

# Create your views here.
def book (request):
    '''
    Render the book page
    '''
    return render(request, 'book/book.html')
