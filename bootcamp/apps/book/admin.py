from django.contrib import admin

# Register your models here.
from apps.book.models import Category, Book
# Register your models here.
admin.site.register(Book)
admin.site.register(Category)