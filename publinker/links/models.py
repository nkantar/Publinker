from django.db import models


class Link(models.Model):
    key = models.CharField(max_length=255, unique=True, blank=False, null=False)
    url = models.URLField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.key} [{self.url}]"

    @classmethod
    def find_by_key(cls, key):
        return cls.objects.get(key=key)
