from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=200, verbose_name='Price')
    pc_description = models.CharField(max_length=200, verbose_name='Description')
    # cms_css = models.CharField(max_length=200, verbose_name='CSS class', null=True, default='-')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.pc_value

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Service')
    pt_old_price = models.CharField(max_length=200, verbose_name='Old Price')
    pt_new_price = models.CharField(max_length=200, verbose_name='New Price')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.pt_title

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
