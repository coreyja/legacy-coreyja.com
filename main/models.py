from django.db import models


class ProjectPicture(models.Model):

    picture = models.ImageField(upload_to='./project-pics/')
    is_thumbnail = models.BooleanField(default=False)


class Project(models.Model):

    name = models.TextField(verbose_name='Project Name', name='Name')
    description = models.TextField()

    pictures = models.ManyToManyField(ProjectPicture)
