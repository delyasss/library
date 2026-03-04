from django.db import models


class Author(models.Model):
    """Автор. Связь One-to-Many с Book (ForeignKey в Book)."""
    first_name = models.CharField('имя', max_length=50)
    last_name = models.CharField('фамилия', max_length=50)
    birth_year = models.IntegerField('год рождения', null=True, blank=True)
    country = models.CharField('страна', max_length=50, null=True, blank=True)
    bio = models.TextField('биография', null=True, blank=True)
    created_at = models.DateTimeField('создан', auto_now_add=True)

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    """Жанр. Связь Many-to-Many с Book."""
    name = models.CharField('название', max_length=100)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Book(models.Model):
    """Книга. ForeignKey -> Author, ManyToMany -> Genre."""
    title = models.CharField('название', max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='автор'
    )
    publication_year = models.IntegerField('год издания', null=True, blank=True)
    pages = models.IntegerField('страниц', null=True, blank=True)
    price = models.DecimalField(
        'цена',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    in_stock = models.BooleanField('в наличии', default=True)
    genres = models.ManyToManyField(
        Genre,
        related_name='books',
        blank=True,
        verbose_name='жанры'
    )
    created_at = models.DateTimeField('добавлена', auto_now_add=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title']

    def __str__(self):
        return self.title


class Reader(models.Model):
    """Читатель. OneToOne с ReaderProfile."""
    first_name = models.CharField('имя', max_length=50)
    last_name = models.CharField('фамилия', max_length=50)
    email = models.EmailField('email', unique=True)
    registered_at = models.DateTimeField('дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'читатель'
        verbose_name_plural = 'читатели'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ReaderProfile(models.Model):
    """Профиль читателя. One-to-One с Reader."""
    reader = models.OneToOneField(
        Reader,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='читатель'
    )
    phone = models.CharField('телефон', max_length=20, null=True, blank=True)
    address = models.TextField('адрес', null=True, blank=True)

    class Meta:
        verbose_name = 'профиль читателя'
        verbose_name_plural = 'профили читателей'

    def __str__(self):
        return f'Профиль: {self.reader}'


class Loan(models.Model):
    """Выдача книги. ForeignKey -> Book, ForeignKey -> Reader."""
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='loans',
        verbose_name='книга'
    )
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE,
        related_name='loans',
        verbose_name='читатель'
    )
    loan_date = models.DateField('дата выдачи')
    return_date = models.DateField('дата возврата', null=True, blank=True)
    returned = models.BooleanField('возвращена', default=False)

    class Meta:
        verbose_name = 'выдача'
        verbose_name_plural = 'выдачи'
        ordering = ['-loan_date']

    def __str__(self):
        return f'{self.book} — {self.reader}'
