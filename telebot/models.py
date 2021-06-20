from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Token')
    tg_chat = models.CharField(max_length=200, verbose_name='Chat Id')
    tg_message = models.TextField(verbose_name='Text message')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.tg_chat

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'