from django.contrib import admin
from book.models import book, Comment

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['book', 'content']
    list_display_links = ['book']
    list_filter = ['book', 'content']
    search_fields = ['content']
    list_editable = ['content']
    
    
    class Meta:
        model = Comment




admin.site.register(book)
admin.site.register(Comment)

