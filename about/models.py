from django.db import models

# Create your models here.

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
