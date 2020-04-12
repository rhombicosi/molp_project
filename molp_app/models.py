from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=100)
    xml = models.FileField(upload_to='problems/xmls/')

    jobNumber = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    result = models.FileField(upload_to='problems/solutions/', blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.xml.delete()
        self.result.delete()
        super().delete(*args, **kwargs)