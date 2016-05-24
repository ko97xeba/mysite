from django.db import models

class Post(models.Model): #django hat spezielle Datentypen
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title # um den wirklichen string value Titel zu bekommen


