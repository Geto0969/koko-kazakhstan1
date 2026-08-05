from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', unique=True, max_length=100)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория',
    )
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', unique=True, max_length=200)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    short_description = models.CharField('Краткое описание', max_length=300)
    description = models.TextField('Описание')
    characteristics = models.TextField('Характеристики', blank=True)
    usage = models.TextField('Способ применения', blank=True)
    image = models.URLField('Изображение (URL)', max_length=500)
    image_alt = models.CharField('Alt текст', max_length=200, blank=True)
    is_featured = models.BooleanField('На главной', default=False)
    is_active = models.BooleanField('Активен', default=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Review(models.Model):
    author_name = models.CharField('Имя', max_length=100)
    text = models.TextField('Отзыв')
    rating = models.PositiveSmallIntegerField('Оценка', default=5)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['order', '-id']

    def __str__(self):
        return f'{self.author_name} — {self.rating}★'


class FAQ(models.Model):
    question = models.CharField('Вопрос', max_length=300)
    answer = models.TextField('Ответ')
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        ordering = ['order']

    def __str__(self):
        return self.question


class SiteSettings(models.Model):
    whatsapp_number = models.CharField(
        'WhatsApp номер',
        max_length=20,
        default='77001234567',
        help_text='Формат: 77001234567 (без +)',
    )
    instagram_url = models.URLField(
        'Instagram',
        default='https://www.instagram.com/koko.kazakhstan/',
    )
    address = models.CharField(
        'Адрес',
        max_length=300,
        default='г. Алматы, ул. Примерная, 1',
    )
    working_hours = models.CharField(
        'Время работы',
        max_length=200,
        default='Пн–Сб: 10:00–20:00, Вс: 11:00–18:00',
    )
    site_title = models.CharField(
        'Title сайта',
        max_length=200,
        default='KOKO Kazakhstan — Корейская косметика',
    )
    site_description = models.TextField(
        'Description',
        default='Профессиональная корейская косметика для здоровой и сияющей кожи. '
        'Оригинальная продукция, доставка по Казахстану.',
    )

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Настройки сайта'

    @classmethod
    def get_settings(cls):
        settings_obj, _ = cls.objects.get_or_create(pk=1)
        return settings_obj
