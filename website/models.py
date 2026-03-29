from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_data']
    def __str__(self):
        return self.name


class newslatters(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
        