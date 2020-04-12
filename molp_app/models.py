from django.db import models

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=100)
    xml = models.FileField(upload_to='problems/xmls/')

    jobNumber = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.xml.delete()
        super().delete(*args, **kwargs)