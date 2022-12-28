from django.db import models

class Createpoll(models.Model):
    que = models.TextField(max_length=500, null=True)
    opt1 = models.CharField(max_length=100, null=True)
    opt2 = models.CharField(max_length=100, null=True)
    opt3 = models.CharField(max_length=100, null=True)
    vo1 = models.IntegerField(null=True, default=0)
    vo2 = models.IntegerField(null=True, default=0)
    vo3 = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.que

