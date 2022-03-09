from django.db import models

# Create your models here.
class ParaPdf(models.Model):
    pdf_file = models.FileField(upload_to="ParaPdfs")