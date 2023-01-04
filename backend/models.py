from django.db import models

class AsosiyMahsulotlar(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    img = models.TextField()

    def __str__(self) -> str:
        return self.name


class BarchaToifalar(models.Model):
    name = models.CharField(max_length=20)
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20)
    type3 = models.CharField(max_length=20)
    type4 = models.CharField(max_length=20)
    number1 = models.IntegerField(default=10)
    number2 = models.IntegerField(default=10)
    number3 = models.IntegerField(default=10)
    number4 = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.name

