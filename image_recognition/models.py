import datetime

from django.utils import timezone
from django.conf import settings
from django.db import models, transaction
from uuslug import slugify

# Create your models here.
class ImageItemsManager(models.Manager):
    def expired(self):
        now = timezone.now()
        return self.filter(
            ImageItems__timestamp__lt = now - datetime.timedelta(
                getattr(settings, 'VERIFICATION_KEY_EXPIRY_DAYS', 4)
            )
        )

    @transaction.atomic
    def delete_expired_users(self):
        for image in self.expired():
            image.delete()

class ImageItems(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    image_init = models.ImageField(default='',upload_to='static/images/%Y/%m/%d')
    image_end = models.ImageField(default='',upload_to='static/images/%Y/%m/%d')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = ImageItemsManager()

    def __str__(self):
        return str(self.image_init)

    class Meta:
        ordering = ["-timestamp"]