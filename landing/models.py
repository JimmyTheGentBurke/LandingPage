from django.db import models

class Subscriber(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(max_length=80, verbose_name='Email')
    context = models.TextField(max_length=200, verbose_name='Текст')

    class Meta:
        verbose_name_plural = 'Subscribers'
        verbose_name = 'Subscriber'
