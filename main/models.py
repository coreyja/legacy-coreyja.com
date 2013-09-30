from django.db import models
from django.template.defaultfilters import slugify


class ProjectPicture(models.Model):

    picture = models.ImageField(upload_to='./project-pics/')
    is_thumbnail = models.BooleanField(default=False)


class ProjectTag(models.Model):
    name = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(ProjectTag, self).save(*args, **kwargs)


class Project(models.Model):

    name = models.TextField(verbose_name='Project Name', name='Name')
    description = models.TextField()
    short_description = models.TextField()

    pictures = models.ManyToManyField(ProjectPicture, related_name="projects")

    tags = models.ManyToManyField(ProjectTag, related_name="projects")

