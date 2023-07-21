from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name

