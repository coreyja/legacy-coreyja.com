from django.db import models
from django.template.defaultfilters import slugify


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
    tags = models.ManyToManyField(ProjectTag, related_name="projects", blank=True, null=True)

    thumbnail = models.ImageField(upload_to='./project-pics/thumbnails/', blank=True, null=True)
    #Has 'pictures' related objects from ProjectPicture model

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_hover_color(self):
        rem = self.id % 5

        colors = ['red', 'purple', 'green', 'orange', 'blue']

        return colors[rem]


class ProjectPicture(models.Model):

    picture = models.ImageField(upload_to='./project-pics/')
    project = models.ForeignKey(Project, related_name="pictures", blank=True, null=True)

    def __unicode__(self):
        return self.picture.name