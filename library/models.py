from django.db import models
from accounts.models import Course, User


class Book(models.Model):
    title = models.TextField(blank=True, default="Название_Книги")
    author = models.TextField(blank=True, default="Автор_Книги")
    pages = models.IntegerField(blank=True, default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author}"


class NoteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} - {self.date_time}"