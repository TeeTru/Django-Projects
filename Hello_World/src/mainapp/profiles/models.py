from django.db import models


class Profile(models.Model):
    First_name = models.Charfield(max-length=50, default="", blank=True, null=False)
    Last_name = models.Charfield(max-length=50, default="", blank=True, null=False)
    Email = models.Charfield(max-length=60, default="", blank=True, null=False)
    Username = models.Charfield(max-length=60, default=""blank=True, null=False)