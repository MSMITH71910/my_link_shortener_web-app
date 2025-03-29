from django.db import models
from django.utils.text import slugify

class Link(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or self.url} ({self.slug})"
    
    def click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        # Generate a slug if it doesn't exist
        if not self.slug:
            base_slug = slugify(self.name or self.url)
            slug = base_slug
            counter = 1
            # Ensure the slug is unique
            while Link.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)