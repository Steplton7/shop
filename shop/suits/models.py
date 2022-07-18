from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории/Каталог товаров"""
    name = models.CharField('Категория', max_length=100)
    url = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Теги"""
    name = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Type(models.Model):
    """Тип одежды"""
    name = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'


class Product(models.Model):
    """Товар/Продукт"""
    title = models.CharField('Название', max_length=200)
    image = models.ImageField(upload_to='articles/')
    description = models.TextField('Описание')
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.SET_NULL,
        null=True
    )
    type = models.ManyToManyField(Type, related_name='product')
    tags = models.ManyToManyField(Tag, related_name="product")
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comment(models.Model):
    """Коментарии"""
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    prod = models.ForeignKey(
        Product,
        related_name="comment",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
