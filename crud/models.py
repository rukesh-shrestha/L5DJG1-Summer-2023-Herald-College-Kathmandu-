from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    

    def __str__(self):
        return self.title


class Contacts(models.Model):
    
    name = models.CharField(max_length=150)
    email=models.EmailField()


    def __str__(self):
        return self.name
