from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Photo = models.ImageField(upload_to='contacts_photo/', blank=True, null=True)

    def __str__(self):
        return f'{self.Name} {self.Surname}'