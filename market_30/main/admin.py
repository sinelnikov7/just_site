from django.contrib import admin

# Register your models here.
from main.models import Category, Product, Magazin, TimeOpen




class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'discription', 'price', 'created', 'update', 'categories', 'image')
    list_display_links = ('title', 'discription')
    search_fields = ('title', 'discription')

admin.site.register(Category)
admin.site.register(Product, BbAdmin)
admin.site.register(Magazin)
admin.site.register(TimeOpen)