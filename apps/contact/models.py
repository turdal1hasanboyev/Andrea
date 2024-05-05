from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=250, blank=True,null=True)
    image = models.ImageField(null=True, blank=True)
    adress = models.CharField(max_length=250, null=True, blank=True)
    web_site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name