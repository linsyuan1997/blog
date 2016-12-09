from django.contrib import admin
from book.models import book

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['book', 'content']
    list_display_links = ['book']
    list_filter = ['book', 'content']
    search_fields = ['content']
    list_editable = ['content']
    
    

       

