from django.db import models
from django.urls import reverse
import uuid  # Required for unique book instances


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Введите описание")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/book1/%s/" % self.pk


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный идентификатор для этой конкретной книги во всей библиотеке")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Техническое обслуживание'),
        ('o', 'Во временном использовании'),
        ('a', 'Доступна'),
        ('r', 'Зарезервирована'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Доступность книги')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Thing(models.Model):
    first = models.CharField(max_length=100)
    second = models.CharField(max_length=100)

    def __str__(self):
        return self.second


class Something(models.Model):
    thing = models.ForeignKey(Thing, on_delete=models.PROTECT)

    def __str__(self):
        return self.thing.first

class Expansion(models.Model):
    active = models.BooleanField(default=False, verbose_name="Активен", help_text="Выберите статус")
    abc = models.OneToOneField(Thing, on_delete=models.CASCADE)
