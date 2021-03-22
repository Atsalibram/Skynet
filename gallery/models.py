from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=60)

    def save_category(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        pgallery = cls.objects.filter(name__icontains=search_term)
        return pgallery

    def __str__(self):
        return self.name

class Location(models.Model):
    location=models.CharField(max_length=60)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.location 