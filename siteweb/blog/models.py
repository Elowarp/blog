from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug_name = models.SlugField(primary_key=True)                   # Url assignée à l'article
    summup = models.CharField(max_length=100)
    text = models.TextField()
    banner = models.ImageField(upload_to="article_images/")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    last_modified_date = models.DateTimeField("date last modified", 
                                              auto_now=True)
    
    def __str__(self):
        return self.slug_name