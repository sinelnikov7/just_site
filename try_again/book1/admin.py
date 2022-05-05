from django.contrib import admin

from book1.models import Genre, Book, BookInstance, Author, Thing, Something, Expansion

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Thing)
admin.site.register(Something)
admin.site.register(Expansion)

# Register your models here.
