from django.db import models

# Create your models here.

class Author(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    blog_content = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="article/",null=True,blank=True)
    datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title