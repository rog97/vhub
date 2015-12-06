from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from vote.managers import VotableManager
# Create your models here

class Startup(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True) #unique=True
    # founders = models.CharField(max_length=100, default=True)
    # investors = models.CharField(max_length=200, default=True)
    # # total_funding = models.DecimalField(max_digits=50, decimal_places=1, default=0)
    # latest_funding = models.DecimalField(max_digits=50, decimal_places=1, default=0)
    description = models.TextField()
    votes = VotableManager()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('startup_edit', kwargs={'pk': self.pk})

def startup_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(startup_pre_save_receiver, sender=Startup)
