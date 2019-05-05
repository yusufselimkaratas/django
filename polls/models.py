import datetime

from django.db import models
from django.utils import timezone

class Sorular(models.Model):

    soru_metni=models.CharField(max_length=200)
    tarih     =models.DateTimeField('tarihi')
    def __str__(self):
        return self.soru_metni
    def was_published_recently(self):
        return self.tarih>= timezone.now()-datetime.timedelta(days=1)
class Secim(models.Model):
     soru    =models.ForeignKey(Sorular, on_delete=models.CASCADE)
     secim_metni = models.CharField(max_length=200)
     oylar  =models.IntegerField(default=0)
     def __str__(self):
         return self.secim_metni
# Create your models here.
