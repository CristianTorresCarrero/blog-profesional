from django.db import models

# Create your models here.

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image_profile = models.ImageField(upload_to='profile_images/')
    cv_pdf = models.FileField(upload_to='cv_pdfs/')

    def __str__(self):
        return self.name  # Muestra el nombre en el panel de administración
