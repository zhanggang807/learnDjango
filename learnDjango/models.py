from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return 'name:' + self.name + ',age:' + str(self.age)
# 待续 python manage.py
