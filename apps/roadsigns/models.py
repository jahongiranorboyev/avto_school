from django.db import models
from apps.utils.models import BaseModel

class RoadSign(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="roadsigns/images/", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.title
