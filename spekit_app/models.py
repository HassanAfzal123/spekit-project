from django.db import models

# Create your models here.
class Topics(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField('Topic Name', max_length=120)

class Folders(models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField('Folder Name', max_length=120)
    folder_description = models.CharField('Folder Description', max_length=255)

class Documents(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField('Document Name', max_length=120)
    doc_path = models.CharField('Document Location', max_length=255)
    folder_id = models.ForeignKey(Folders, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE)