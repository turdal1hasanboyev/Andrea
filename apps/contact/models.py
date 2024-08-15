from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    