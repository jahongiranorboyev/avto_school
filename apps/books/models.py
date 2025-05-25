from django.conf import settings
from django.db import models

from apps.utils.models import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="book/icons/", null=True, blank=True)

    def __str__(self):
        return self.title


class BookChapter(BaseModel):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to="book/audio/", null=True, blank=True)
    pdf_file = models.FileField(upload_to="book/pdf/", null=True, blank=True)

    def __str__(self):
        return self.title


class BookPage(BaseModel):
    book_chapter = models.ForeignKey('books.BookChapter', on_delete=models.CASCADE)
    content = models.TextField()
    page_order = models.IntegerField()

    def __str__(self):
        return self.page_order


class UserBookChapter(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_chapter = models.ForeignKey('books.BookChapter', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.id}'
