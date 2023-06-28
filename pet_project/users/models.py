from django.db import models
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator


class CustomUser(AbstractUser):
    USER = 'users'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    USER_ROLES = [
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]
    username = models.CharField(
        'Никнейм',
        max_length=150,
        unique=True,
        help_text='Введите ваш никнейм',
        validators=[UnicodeUsernameValidator],
        blank=False,
        error_messages={
            'unique': 'Пользователь с таким никнеймом уже существует',
        },
    )
    email = models.EmailField(
        'Адрес электронной почты',
        help_text='Введите адрес электронной почты',
        max_length=254,
        unique=True,
        blank=False
    )
    first_name = models.CharField(
        'Имя',
        help_text='Введите имя',
        max_length=150,
        blank=False
    )
    last_name = models.CharField(
        'Фамилия',
        help_text='Введите фамилию',
        max_length=150,
        blank=False
    )
    password = models.CharField(
        max_length=150,
        blank=False
    )
    phone_number = models.CharField(
        'Номер телефон',
        help_text='Введите номер телефона',
        max_length=20,
        blank=False
    )
    city = models.TextField(
        'Город',
        help_text='Укажите Ваш город',
        max_length=30,
        blank=False
    )
    age = models.PositiveSmallIntegerField(
        'Возраст',
        help_text='Укажите Ваш возраст',
        null=True,
        blank=True
    )
    image = models.ImageField(
        'Фото',
        upload_to='cars/images/users/',
        help_text='Добавьте Ваше фото',
    )
    role = models.CharField(choices=USER_ROLES,
                            default=USER,
                            max_length=25,
                            blank=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    def __str__(self):
        return self.username
