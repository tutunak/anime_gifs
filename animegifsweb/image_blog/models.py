from django.db import models
from django.utils import timezone

class Publication(models.Model):
    publication_date = models.DateTimeField(default=timezone.now, name='date published')
    published = models.BooleanField(default=False)
    publication_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pk + " " + self.publication_name

class Gif(models.Model):
    publication_id = models.ForeignKey(Publication, on_delete=models.CASCADE)
    path = models.CharField(max_length=256)
    gif_name = models.CharField(max_length=200)

    def __str__(self):
        return self.gif_name

class RssUrl(models.Model):
    rss_url = models.URLField('Rss source', unique = True)
    rss_name = models.CharField("Name", max_length = 200)
    active = models.BooleanField(default = 0)
    last_post = models.DateTimeField('Last checked post', blank = True, null=True)

    def __str__(self):
        return str(self.id) + " " + self.rss_name