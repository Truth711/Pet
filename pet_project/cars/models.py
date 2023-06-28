from django.db import models
from users.models import CustomUser


class Brand(models.Model):
    name = models.CharField(
        'Название брэнда',
        max_length=200,
        unique=True,
    )
    country = models.CharField(
        'Страна',
        max_length=200,
    )
    description = models.TextField(
        'Описание',
    )
    logo = models.ImageField(
        'Изображение логотипа',
        upload_to='cars/images/logo/'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class Car(models.Model):
    MANUAL = 'manual'
    AUTOMATIC = 'automatic'
    TRANSMISSION_CHOICES = (
        (MANUAL, 'Ручная'),
        (AUTOMATIC, 'Автоматическая'),
    )
    SEDAN = 'sedan'
    HATCHBACK = 'hatchback'
    SUV = 'SUV'
    PICKUP = 'pickup'
    LIMOUSINE = 'limousine'
    SPECIAL_EQUIPMENT = 'special equipment'
    CAR_BODY_CHOICES = (
        (SEDAN, 'Седан'),
        (HATCHBACK, 'Хэтчбек'),
        (SUV, 'Внедорожник'),
        (PICKUP, 'Пикап'),
        (LIMOUSINE, 'Лимузин'),
        (SPECIAL_EQUIPMENT, 'Спецтехника'),
    )
    name = models.CharField(
        'Название модели авто',
        help_text='Введите полное название модели авто',
        max_length=200,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name='Марка автомобиля',
    )
    color = models.CharField(
        'Цвет в HEX',
        max_length=7,
    )
    transmission = models.CharField(
        'Коробка передач',
        help_text='Выберите коробку передач',
        choices=TRANSMISSION_CHOICES,
        max_length=25,
    )
    car_body = models.CharField(
        'Кузов',
        help_text='Выберите кузов автомобиля',
        choices=CAR_BODY_CHOICES,
        max_length=25,
    )
    mileage = models.PositiveIntegerField(
        'Пробег',
        help_text='Введите пробег в км',
    )
    price = models.PositiveIntegerField(
        'Цена',
        help_text='Введите цену в рублях',
    )
    seller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='cars',
        verbose_name='Продавец',
    )
    overview = models.TextField(
        'Комментарии продавца',
        help_text='Добавьте комментарии (опционально)',
        blank=True,
    )
    image = models.ImageField(
        'Изображение автомобиля',
        upload_to='cars/images/cars/',
        help_text='Добавьте изображение',
    )
    pub_date = models.DateTimeField(
        'Дата публикации объявления',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.name


class Favorites(models.Model):
    """Модель для связи юзера с его списком понравившихся предложений."""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Понравившееся предложение',
    )

    class Meta:
        verbose_name = 'Понравившееся предложение'
        verbose_name_plural = 'Избранное'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'car'),
                name='unique-car-in-favorites'
            ),
        )

    def __str__(self):
        return f'{self.user} добавил в избранное {self.car}'
