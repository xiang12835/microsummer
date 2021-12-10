from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def to_json(self):
        d = {
            "name": self.name,
            "age": self.age,
        }
        return d
