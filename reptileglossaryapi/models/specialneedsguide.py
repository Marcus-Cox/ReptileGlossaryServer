from django.db import models
from django.db import models
from .writer import Writer
from .specialneedsreptile import SpecialNeedsReptile

class SpecialNeedsGuide(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    specialneedsreptile = models.ForeignKey(SpecialNeedsReptile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    publishing_date = models.DateField(auto_now_add=True)
    