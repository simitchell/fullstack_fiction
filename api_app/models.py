from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(null=True)
    author = models.CharField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        #  string for representing the model object.  A book!
        return self.title