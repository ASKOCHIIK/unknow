from django.db import models


class Tovar(models.Model):
    title = models.CharField('Название товара', max_length=250)
    price = models.IntegerField('Цена')


class TovarImage(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE, related_name='img')
    img = models.ImageField('Изображении', upload_to='tovar/%m')
