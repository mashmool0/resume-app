from django.db import models
import jdatetime
import random 


# Create your models here.
list_month = ['', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد',
              'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

month = list_month[int(str(jdatetime.date.today()).split('-')[1])]
day = str(jdatetime.date.today()).split('-')[2]



class Blog_post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cover = models.ImageField(default='False')
    month_def = models.CharField(max_length=20,default=month) 
    day_def = models.CharField(max_length=20,default=day)
    randomkey = models.CharField(default=random.randint(2000,2100),max_length=5)
    
    def __str__(self) -> str:
        return self.title