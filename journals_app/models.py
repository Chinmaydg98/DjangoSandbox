from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Journal(models.Model):
    """
    A Journal holds entries, which in turn hold topics
    Hierarchy is as follows:
        JOURNAL -(contain)-> ENTRIES -(contain)-> TOPICS
    """
    title = models.TextField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Simply returns name of Journal"""
        return str(self.title).upper()


class Entry(models.Model):
    """
    An entry belongs to a Journal
    An entry includes Topics
    """
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return content in short"""
        return str(self.text[:50])

    class Meta:
        verbose_name_plural = 'entries'


class Topic(models.Model):
    """
    A topic belongs to an Entry.
    """
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        """Return content in short"""
        return str(self.text[:50])

    class Meta:
        verbose_name_plural = 'Topics'
