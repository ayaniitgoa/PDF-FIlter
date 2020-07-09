from django.db import models

# Create your models here.


class Files(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs')

    def __str__(self):
        return self.name
