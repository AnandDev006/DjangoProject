from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    fullName = models.CharField( blank = True, null = True, max_length = 30)
    timeStamp = models.DateTimeField( auto_now_add = True, auto_now = False)
    updated = models.DateTimeField( auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name_plural = "SignUp"

    def __str__(self):
        return self.fullName
