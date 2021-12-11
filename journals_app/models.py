from django.db import models


# Create your models here.
class Journal(models.Model):
    """
    A Journal holds entries, which in turn hold topics
    Hierarchy is as follows:
        JOURNAL -(contain)-> ENTRIES -(contain)-> TOPICS
    """
    title = models.TextField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Simply returns name of Journal"""
        return str(self.title).upper()
