from django.db import models

class SimpleModel(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='https://www.google.com')
    
    def __str__(self):
        return self.text
    
class Language(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.col or "Vacío"

class Framework(models.Model):
    name = models.CharField(max_length=15)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name