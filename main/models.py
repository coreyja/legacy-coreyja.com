from django.db import models
from django.template.defaultfilters import slugify

import random


class ProjectPicture(models.Model):

    picture = models.ImageField(upload_to='./project-pics/')
    is_thumbnail = models.BooleanField(default=False)


class ProjectTag(models.Model):
    name = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(ProjectTag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Project(models.Model):

    name = models.TextField(verbose_name='Project Name')
    description = models.TextField()
    short_description = models.TextField()

    pictures = models.ManyToManyField(ProjectPicture, related_name="projects", blank=True, null=True)

    tags = models.ManyToManyField(ProjectTag, related_name="projects", blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_hover_color(self):
        rem = self.id % 5

        colors = ['red', 'purple', 'green', 'orange', 'blue']

        return colors[rem]

    def thumbnail_url(self):
        thumbnails = self.pictures.filter(is_thumbnail=True)
        if thumbnails:
            return thumbnails[0].picture.url

        return False

