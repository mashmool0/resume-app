from django.db import models
import jdatetime
# Create your models here.


class Mail(models.Model):
    FullName = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    text = models.TextField()
    date = models.CharField(default=str(jdatetime.date.today()),max_length=20,null=True)

    def __str__(self) -> str:
        return self.email
