from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=255, blank=False)
    subdomain = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    