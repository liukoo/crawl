from django.db import models
class Queue(models.Model):
    url = models.URLField()
    mail = models.CharField(max_length=100)
    sales = models.IntegerField(blank=True,default=0)
    money = models.IntegerField(blank=True,default=0)
    stat = models.IntegerField(blank=True,default=0)
    time = models.DateTimeField()
    def __unicode__(self):
        return str(self.id)
# Create your models here.
