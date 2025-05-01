from django.contrib import admin
from .models import Book, BookChapter, BookPage, UserBookChapter

class BookInline(admin.TabularInline):
    model = Book

class BookChapterInline(admin.TabularInline):
    model = BookChapter


class BookPageInline(admin.TabularInline):
    model = BookPage

class UserBookChapterInline(admin.TabularInline):
    model = UserBookChapter


admin.site.register(Book)
admin.site.register(BookChapter)
admin.site.register(BookPage)
admin.site.register(UserBookChapter)