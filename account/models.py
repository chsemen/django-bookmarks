from django.db import models
from django.conf import settings

# Create your models here.
# admin
# funtik123

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True
    )

    def __str__(self) -> str:
        return f'Profile of {self.user.username}'
