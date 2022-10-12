from django.contrib import admin

# Register your models here.
from apps.book.models import Category, Book
# Register your models here.
admin.site.register(Book)#SE REGISTRA LA CLASE LIBRO
admin.site.register(Category)#SE REGISTRA LA CLASE CATEGORIA
