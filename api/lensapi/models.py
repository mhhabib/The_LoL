import uuid
from PIL import Image
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def thumbnail_image_upload_to(instance, filename):
        ext = filename.split('.')[-1]
        unique_name = f"{uuid.uuid4().hex}.{ext}"
        return f'thumbnails/{unique_name}'

    thumbnail_image = models.ImageField(upload_to=thumbnail_image_upload_to, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.thumbnail_image.path)
        img.thumbnail((424, 320))
        img.save(self.thumbnail_image.path)