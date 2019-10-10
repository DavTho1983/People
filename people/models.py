from django.db import models

class Person(models.Model):
    class Meta:
        verbose_name_plural = "Persons"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name
