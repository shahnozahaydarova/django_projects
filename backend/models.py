from django.db import models

class MaishiyTehnikalar(models.Model): 

    class Meta:
        verbose_name = 'Maishiy Tehnika'
        verbose_name_plural = 'Maishiy Tehnikalar'

    name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    img = models.TextField()

    def __str__(self) -> str:
        return self.name


class Mebellar(models.Model):
    class Meta:
        verbose_name = 'Mebel'
        verbose_name_plural = 'Mebellar'

    name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    img = models.TextField()

    def __str__(self) -> str:
        return self.name


class BarchaToifalar(models.Model):
    class Meta:
        verbose_name = 'Barcha Mahsulot turlari'
        verbose_name_plural = 'Barcha Mahsulot turlari'


    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50)
    type3 = models.CharField(max_length=50)
    type4 = models.CharField(max_length=50)
    number1 = models.IntegerField(default=500)
    number2 = models.IntegerField(default=500)
    number3 = models.IntegerField(default=500)
    number4 = models.IntegerField(default=500)

    def __str__(self) -> str:
        return self.name


class MaishiyTehnikalarSoni(models.Model):
    class Meta:
        verbose_name = 'Maishiy Tehnikalar soni'
        verbose_name_plural = 'Maishiy Tehnikalar soni'
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class MebellarSoni(models.Model):
    class Meta:
        verbose_name = 'Mebellar soni'
        verbose_name_plural = 'Mebellar soni'
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.name





