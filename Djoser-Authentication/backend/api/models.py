from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title