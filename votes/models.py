from django.db import models

# Create your models here.
class Vote(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    vote_taken = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    ayes = models.IntegerField(blank=False)
    nays = models.IntegerField(blank=False)