from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """Модели обратной связи"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class ContactLink(models.Model):
    """Класс модели контактов"""
    #icon = models.FileField(upload_to="icons/", blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class About(models.Model):
    mini_text = RichTextField()
    text = RichTextField()

    def __str__(self):
        return self.mini_text

    class Meta:
        verbose_name = 'Текст о нас'
        verbose_name_plural = 'О нас'

class ImageAbout(models.Model):
    image = models.ImageField(upload_to="about/")
