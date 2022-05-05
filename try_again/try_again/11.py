from django.contrib import admin
from django.urls import path

#from book1.views import rot
#from book1.models import Book
from ..book1.models import Book
from ..book1.views import rot

s = Book.get_absolute_url(Book)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', rot),
    path(s, rot)
]
print(s)