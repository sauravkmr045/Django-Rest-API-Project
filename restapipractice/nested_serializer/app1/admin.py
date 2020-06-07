from django.contrib import admin
from app1.models import Author, Book
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	model= Author
	list_display = ['id','first_name','last_name','subject']

class BookAdmin(admin.ModelAdmin):
	model = Book
	list_display = ['id','title','author','release_date','rating']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
