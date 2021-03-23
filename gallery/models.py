from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=60)

    def save_category(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        gallery = cls.objects.filter(name__icontains=search_term)
        return gallery

    def __str__(self):
        return self.name

class Location(models.Model):
    location=models.CharField(max_length=60)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.location 

class Image(models.Model):
    image=models.ImageField(upload_to='gallery/', blank=True)
    image_link=models.TextField(blank=True)
    image_name=models.TextField(max_length=60 , blank=True)
    details=models.TextField(max_length=60, blank=60)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, blank=True)
    location=models.ForeignKey(Location, blank=True, null=True,on_delete = models.CASCADE)

    def save_image(self):
        self.save()