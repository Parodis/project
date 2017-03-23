from django.db import models


class Delivery(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}, id: {}'.format(self.name, self.id)
# Create your models here.
