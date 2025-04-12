from django.db import models

# Create your models here.
class Contact(models.Model):
    Photo = models.ImageField(upload_to='contacts_photo/', default = 'icon.jpg', blank=True)
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    #object = models.Manager()

    def __str__(self):
        return f'{self.Name}'