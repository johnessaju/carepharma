from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    password = models.CharField(max_length=255)
    mailid = models.EmailField(max_length=255)
    isloggedin = models.BooleanField(default=False)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'Customers'  

    def __str__(self):
        return self.name