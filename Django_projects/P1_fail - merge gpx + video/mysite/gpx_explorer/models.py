from django.db import models


class GPX_File(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='%Y/%m/%d/')
    upload_date = models.DateField(auto_now=True)


class Contact_Form(models.Model):
    mail = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
