from django.db import models

TYPE_PREFIX = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Dr', 'Dr'),
}


class Profile(models.Model):
    Prefix = models.CharField(max_length=4, choices=TYPE_PREFIX)
    First_name = models.CharField(max_length=50, default="", blank=True, null=False)
    Last_name = models.CharField(max_length=50, default="", blank=True, null=False)
    Email = models.CharField(max_length=60, default="", blank=True, null=False)
    Username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.First_name
