from django.db import models


# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Status')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.Status_name

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.order_name

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    comment_text = models.TextField(verbose_name='Comment Text')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Creation date')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.comment_text

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
