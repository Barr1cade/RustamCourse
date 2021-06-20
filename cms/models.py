from django.db import models


# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/', blank=True)
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, verbose_name='CSS class', null=True, default='-')

    def __str__(self):
        """Возвращает название нашего класса"""
        return self.cms_title

    class Meta:
        """возвращает нужное нам написание полей"""
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
